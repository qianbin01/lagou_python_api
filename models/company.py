from models import company


def get_company_list(page=1):
    if not page:
        page = 1
    companies = company.find().limit(10).skip(10 * int(page))
    data_list = []
    for item in companies:
        item['_id'] = str(item['_id'])
        data_list.append(item)
    return data_list
