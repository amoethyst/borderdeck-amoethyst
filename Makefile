.PHONY: separated userstyle all

all: separated userstyle

separated: build/iframes.css build/style.css

userstyle: build/userstyle.css build/test.css

clean:
	rm -r build/


build/iframes.css: iframes.css
	./generate.py iframes.css

build/style.css: style.css
	./generate.py style.css

build/userstyle.css: style.css iframes.css
	@mkdir -p build
	@printf '@namespace url(http://www.w3.org/1999/xhtml);\n\n@-moz-document domain("tweetdeck.twitter.com") {\n' > build/userstyle.css
	@cat style.css >> build/userstyle.css
	@printf '\n}\n\n@-moz-document regexp("https?://twitter.com/i/cards/.*") {\n' >> build/userstyle.css
	@cat iframes.css >> build/userstyle.css
	@printf '\n}' >> build/userstyle.css
	@echo created build/userstyle.css

build/test.css: build/userstyle.css generate.py
	./generate.py build/userstyle.css test.css

