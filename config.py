import os #i import this so that i can get my api key from the venv environment. Now request.py gets it from importing Config

class Config:
    ''''''

    MY_API_KEY = os.environ.get('MY_API_KEY')
    MY_BASE_URL = 'https://newsapi.org'
    ARTICLES = MY_BASE_URL + \
        '/v2/everything?sources={}&apikey='+str(MY_API_KEY)
    SOURCES = MY_BASE_URL + \
        '/v2/top-headlines/sources?category={}&apikey=' + str(MY_API_KEY)


class ProdConfig(Config):

    '''Production configuration class'''

    pass


class DevConfig(Config):
    '''Development configuration class'''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
