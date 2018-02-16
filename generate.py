#!/usr/bin/env python3
import re
import sys
import pathlib
import os.path

build = pathlib.Path('build')

prog = re.compile(r"\/\*\[\[(.*?)\]\]\*\/")


desc = {
    'font': "Font to use on TweetDeck",
    'extfont': "external font",
    'color1': "main color",
    'color2': "color on hover for most links and buttons",
    'color3': "color used for scheduled tweets",
    'color4': "color used for input fields and calendar",
    'color5': "color on unfocus of a compose box",
    'bgcolor': "background color",
    'rad': "radius of avatars",
    'filtered_by': "hide the 'Filtered by' message in columns",
    'hide_circle_counter': "Hide the 'circle' counter in compose boxes"
}


class Args(dict):

    def replace(self, matchobj):
        key = matchobj.group(1)
        return self.get(key, matchobj.group(0))


defaults = Args({
    'font': '"Aller"',
    'extfont': "",
    'color1': "#9966cc",
    'color2': "#cc88ff",
    'color3': "#664488",
    'color4': "#332244",
    'color5': "#181224",
    'bgcolor': "#111111",
    'rad': "100%",
    'filtered_by': ".js-column-message {display: none}",
    'hide_circle_counter': ".js-progress-svg {display:none}" 
})


def generate_userstyle(args):
    userstyle = build / "userstyle.css"
    test = build / "test.css"

    with userstyle.open() as stream:
        text = prog.sub(args.replace, stream.read())

    with test.open(mode='w') as f:
        f.write(text)


def generate(path, out=None, **kwargs):
    args = Args(kwargs)
    build.mkdir(exist_ok=True)

    if out is None:
        out = build / path.name
    else:
        out = build / out.name

    with path.open() as stream:
        text = prog.sub(args.replace, stream.read())

    with out.open(mode='w') as f:
        f.write(text)


def main():
    path = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[2]) if len(sys.argv) == 3 else None

    if not path.exists():
        raise RuntimeException("no path given")

    generate(path, out=out, **defaults)


if __name__ == '__main__':
    main()
