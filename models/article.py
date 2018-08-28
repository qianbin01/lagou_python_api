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


def set_articles_commit_by_user():
    pass


def add_article_like():
    pass


def add_commit_like():
    pass
