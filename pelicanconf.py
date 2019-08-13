#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ashley Felton'
SITENAME = 'ropable.com'
SITEURL = ''
#SITEURL = 'https://ropable.com'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Australia/Perth'
DEFAULT_LANG = 'en'

# Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
    ('stack-overflow', 'https://stackoverflow.com/users/14508/ropable'),
    ('github', 'https://github.com/ropable'),
    ('facebook', 'https://www.facebook.com/ropable'),
    ('hacker-news', 'https://news.ycombinator.com/user?id=ropable'),
    #('twitter', 'https://twitter.com/ropable'),
    #('linkedin', 'https://au.linkedin.com/in/AshleyFelton'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'templates/hyde'
PROFILE_IMAGE = 'profile.jpg'
BIO = "I'm Ashley Felton, a full-stack web developer and sysadmin based in Perth, WA."
