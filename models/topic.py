from models import topic


def get_topic_list(page=1):
    if not page:
        page = 1
    topics = topic.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in topics:
        item['_id'] = str(item['_id'])
        item['logo'] = 'www.lgstatic.com/' + item['logo']
        print(item)
        data_list.append(item)
    return data_list
