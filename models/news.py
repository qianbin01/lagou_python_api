from models import news


def get_news_list(page=1):
    if not page:
        page = 1
    newses = news.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in newses:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


def get_single_news(nid):
    if not nid:
        return
    news_item = news.find_one({'nid': int(nid)})
    if news_item:
        news_item['_id'] = str(news_item['_id'])
        return news_item
    return ''


def get_news_count():
    return {
        'total': news.count(),
        'sizeCount': int(news.count() / 10) + 1,
    }
