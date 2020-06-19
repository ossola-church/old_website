#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Chiesa Cristiana Evangelica dell'Ossola"
SITENAME = "Chiesa Cristiana Evangelica dell'Ossola"
SITEURL = ''

PATH = 'content'

THEME = 'tema/pelican-themes/pelican-hyde'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Biography
# BIO = "Gesù: Via, Verità e Vita"
PROFILE_IMAGE = 'avatar.png'


# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email','info@chiesaevangelicaossola.com'),
          ('github', 'https://github.com/ossola-church'),
          ('facebook','https://www.facebook.com/'))


DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Plugins
PLUGIN_PATHS = [ 'plugins/pelican-plugins' ]
PLUGINS = [ 'summary','sitemap' ]


# Struttura sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.7,
        'pages': 0.9
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'weekly'
    }
}

# altro 
DIRECT_TEMPLATES = ['blog']
PAGINATED_DIRECT_TEMPLATES = ['blog']

# file statici 
# STATIC_PATHS = ['images','extra/CNAME', 'extra/robots.txt']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
#                        'extra/robots.txt': {'path': 'robots.txt'},
#                        }


# Static files
STATIC_PATHS = ['extra','images']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},
                              'extra/CNAME': {'path': 'CNAME'},
                              'extra/robots.txt':{'path': 'robots.txt'}}
