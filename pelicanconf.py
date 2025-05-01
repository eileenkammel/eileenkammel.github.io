from __future__ import unicode_literals

# Basic information
AUTHOR = u'Eileen Kammel'
AUTHOREMAIL = 'eileen@kammel.dev'
SITENAME = 'Large Language Musings'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

THEME = "pelican-themes/graymill"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Best Playlist", "https://open.spotify.com/playlist/6hx11ZpXIunQDCxq6OrHs7?si=bcec27f22e084d15"),
)

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/eileen-kammel/"),
    ("github", "https://github.com/eileenkammel/"),
)

DEFAULT_PAGINATION = 5

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (
    ("Home", "/"),
)

DISPLAY_SUMMARY = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
