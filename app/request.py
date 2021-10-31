import json
from urllib import request
from .models import Source, Article

# Getting api key
ARTICLES = None
# Getting the movie base url
SOURCES = None


def configure_request(app):
    global ARTICLES, SOURCES
    ARTICLES = app.config['ARTICLES']
    SOURCES = app.config['SOURCES']


def get_sources(category):
    path = SOURCES.format(category)
    content = request.urlopen(path)
    jason = json.loads(content.read())
    return jason['sources']


def process_sources(sources):
    list_of_sources = []
    for i in sources:
        s = Source(
            i['id'],
            i['name'],
            i['description'],
            i['url'],
            i['category'],
            i['language'],
            i['country']
        )
        list_of_sources.append(s)
    return list_of_sources


def get_articles(source):
    path = ARTICLES.format(source)
    content = request.urlopen(path)
    jason = json.loads(content.read())
    return jason['articles']


def process_articles(articles):
    list_of_articles = []
    for each in articles:
        a = Article(
            each['source'],
            each['author'],
            each['title'],
            each['description'],
            each['url'],
            each['urlToImage'],
            each['publishedAt'],
            each['content']
        )
        list_of_articles.append(a)
        return list_of_articles
