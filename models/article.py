from models import article


def get_articles_list(tid='', page=1):
    if not page:
        page = 1
    if not tid:
        articles = article.find().limit(10).skip(10 * (int(page) - 1))
    else:
        articles = article.find({'topic_id': tid}).limit(10).skip(10 * (int(page) - 1))
    data_list = []
    for item in articles:
        data_list.append({'news': item.get('news')})
    return data_list


def get_articles_single(aid):
    article_item = article.find_one({'questionId': aid})
    return article_item.get('news')


def get_articles_count():
    return {
        'total': article.count(),
        'sizeCount': int(article.count() / 10) + 1,
    }
