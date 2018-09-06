import models.comment as comment
from flask import Blueprint, jsonify, request

comment_blue_print = Blueprint('comment', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@comment_blue_print.route('/lists')
def lists():
    aid = request.args.get('aid')
    return jsonify({'status': status, 'dataList': comment.get_comment_list(aid)})
