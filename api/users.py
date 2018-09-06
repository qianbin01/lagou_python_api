import models.users as users
from flask import Blueprint, jsonify, request

comment_user_blue_print = Blueprint('comment_user', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@comment_user_blue_print.route('/lists')
def lists():
    aid = request.args.get('aid')
    return jsonify({'status': status, 'dataList': users.get_comment_user_list(aid)})
