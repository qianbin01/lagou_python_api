import models.company as company
from flask import Blueprint, jsonify, request

company_blue_print = Blueprint('company', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}
company_doc = company.get_company_count()


@company_blue_print.route('/lists')
def lists():
    page = request.args.get('page')
    company_doc['index'] = page
    return jsonify(
        {'status': status,
         'pageInfo': company_doc,
         'dataList': company.get_company_list(page)
         })


@company_blue_print.route('/single')
def company_singe():
    cid = request.args.get('cid')
    return jsonify({'status': status, 'object': company.get_company_single(cid)})
