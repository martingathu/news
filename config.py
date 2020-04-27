# import os
# class Config:
#     '''
#     General configuration parent class
#     '''
#     NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
#     ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
#     NEWS_API_KEY ='4884752d29c84db4a7601e9a3a19d7f9'

# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True

# config_options = {
#     "production":ProdConfig,
#     "development": DevConfig }
NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
NEWS_API_KEY ='4884752d29c84db4a7601e9a3a19d7f9'
