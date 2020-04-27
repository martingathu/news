import urllib, json
from app import app
from app.models.news import Source, Article


# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news source and article base url
base_url = app.config["NEWS_SOURCES_BASE_URL"]
base_url_article = app.config["ARTICLES_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        sources_results = None
        if get_source_response['results']:
            sources_results_list = get_source_response['results']
            sources_results = process_results(sources_results_list)
		

    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        county = source_item.get('country')
        
        if url:
            sources_object = Source(id, name, description, url, category, language, county)
            sources_results.append(sources_object)
        
    return sources_results

def get_articles(source_id):
    base_url_article = base_url_article.format(source_id, api_key)
    url_datas = requests.get(url)
    article_dict = url_datas.json()
    articles_list = article_dict.get('articles')

    return process_articles(articles_list)

def process_articles(articles_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    articles = []
    if articles_list:
        for article in articles_list:
            article = Article(article['author'], article['title'], article['description'], article['url'], article['urlToImage'], article['publishedAt'])
            articles.append(article)
        return articles

        message = 'hello world'
        return render_template('index.html', message = message)
        

# def get_news(news_list):
#     '''
#     Function  that processes the news result and transform them to a list of Objects

#     Args:
#         news_list: A list of dictionaries that contain news details

#     Returns :
#         news_results: A list of news objects
#     '''
#     sources_results = []
#     top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')
    
#     articles = top_headlines['articles']

#     desc = []
#     news = []
#     img = []
#     url =[]

#     for i in range(len(articles)):
#         myarticles = articles[i]

#         news.append(myarticles['title'])
#         desc.append (myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         url.append(myarticles['url'])


#     news_list = zip(news, desc, img, url)

#     return render_template('index.html', context = news_list)


