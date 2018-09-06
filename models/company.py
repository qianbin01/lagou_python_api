from models import company
from bson.objectid import ObjectId


def get_company_list(page=1):
    if not page:
        page = 1
    companies = company.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in companies:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list


def get_company_single(cid):
    company_item = company.find_one({'_id': ObjectId(cid)})
    company_item['_id'] = str(company_item['_id'])
    return company_item


def get_company_count():
    return {
        'total': company.count(),
        'sizeCount': int(company.count() / 10) + 1,
    }
