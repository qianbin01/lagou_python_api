from models import article, comment, likes, comment_user


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


def get_article_comments(aid):
    comments = comment.find({'article_id': aid})
    data_list = []
    for item in comments:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


def get_article_comment_user(cid):
    comment_user_one = comment_user.find_one({'answerId': cid})
    if comment_user_one and comment_user_one.get('_id'):
        comment_user_one['_id'] = str(comment_user_one['_id'])
    return comment_user_one


def set_articles_comment_by_user():
    pass


def add_article_like():
    pass


def add_comment_like():
    pass
