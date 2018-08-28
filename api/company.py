import models.company as company
from flask import Blueprint, jsonify

company_blue_print = Blueprint('company', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@company_blue_print.route('/lists/<page>')
def lists(page):
    return jsonify({'status': status, 'dataList': company.get_company_list(page)})
