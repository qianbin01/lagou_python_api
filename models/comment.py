from models import comment


def get_comment_list(aid):
    if not aid:
        return []
    comments = comment.find({'article_id': aid})
    data_list = []
    for item in comments:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list
