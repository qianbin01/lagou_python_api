from models import recruit


def get_recruits_list(page=1):
    if not page:
        page = 1
    recruits = recruit.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in recruits:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


