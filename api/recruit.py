import models.recruit as recruit
from flask import Blueprint, jsonify, request

recruit_blue_print = Blueprint('recruit', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}
recruit_doc = recruit.get_recruit_count()


@recruit_blue_print.route('/lists')
def lists():
    page = request.args.get('page')
    recruit_doc['index'] = page
    return jsonify(
        {'status': status,
         'pageInfo': recruit_doc,
         'dataList': recruit.get_recruits_list(page)
         })


@recruit_blue_print.route('/single')
def recruit_singe():
    rid = request.args.get('rid')
    return jsonify({'status': status, 'object': recruit.get_recruits_single(rid)})
