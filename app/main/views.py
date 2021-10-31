from flask import render_template, request, redirect, url_for
from .views import *
from . import main
from ..request import *

@main.route('/')
def root():
    return redirect(url_for('main.sources'))

@main.route('/sources')
def sources():
    title='sources'
    business_sources=get_sources('business')
    entertainment_sources=get_sources('entertainment')
    general_sources=get_sources('general')
    health_sources=get_sources('health')
    science_sources=get_sources('science')
    sports_sources=get_sources('sports')
    tech_sources=get_sources('technology')

    return render_template('index.html', title=title, business=business_sources,
                           entertainment=entertainment_sources, general=general_sources, health=health_sources,
                           science=science_sources, sports=sports_sources, tech=tech_sources)


@main.route('/articles/<source>')
def articles(source):
    articles = get_articles(source)
    return render_template('articles.html', title=source,articles=articles)