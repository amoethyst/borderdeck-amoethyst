# Borderdeck-amoethyst
A css theme for TweetDeck

Available on <a href=https://userstyles.org/styles/108707/borderdeck-amoethyst>Userstyles</a>.

Set your TweetDeck theme to 'Light' in the settings after installing this
theme.

# Getting started

Requirements: Python 3, make

make might be a bit tricky to get on Windows (but not impossible afaik).

To generate the style you can use this command:

    make

That's it, this will generate some files in the build directory, the most
important one is probably `test.css`, you should be able to import it
easily with your favorite user styles manager.

# Explanation of some files

`style.css` contains the stylesheet for TweetDeck, that's where
most of the things are done. It uses the UserStyles syntax (or whatever
you call it) for elements that can be changed when you are installing
it for userstyles.org. Also, it's quite a mess.

`iframes.css` impacts all the iframes that appear on TweetDeck.
That includes the polls and probably some other things that I forgot.

`generate.py` is a Python script that is used to create the test.css file
to quickly test your changes. This let's me use the UserStyles syntax
while being able to test it before I upload it (that's pretty useful).

# Contribution

I must say that I created this repo so that somebody could fix some bugs
that I just missed or just that I didn't have enough time to look into
yet. So if you see something weird and know a bit of CSS, you can fork
this repository, fix the thing, quickly check that this actually works
by running make and create a pull request.

Well of course if you don't know anything about CSS you can create an
issue, I'll do my best to solve them.

