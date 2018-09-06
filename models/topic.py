from models import topic


def get_topic_list(page=1):
    if not page:
        page = 1
    topics = topic.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in topics:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


def get_single_topic(tid):
    topic_item = topic.find_one({'id': tid})
    topic_item['_id'] = str(topic_item['_id'])
    return topic_item


def get_topic_count():
    return {
        'total': topic.count(),
        'sizeCount': int(topic.count() / 10) + 1,
    }
