from models import recruit
from bson.objectid import ObjectId


def get_recruits_list(page=1):
    if not page:
        page = 1
    recruits = recruit.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in recruits:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


def get_recruits_single(rid):
    recruit_item = recruit.find_one({'_id': ObjectId(rid)})
    recruit_item['_id'] = str(recruit_item['_id'])
    return recruit_item
