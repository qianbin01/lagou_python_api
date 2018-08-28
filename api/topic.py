import models.topic as topic
from flask import Blueprint, jsonify

topic_blue_print = Blueprint('topic', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@topic_blue_print.route('/lists/<page>')
def lists(page):
    return jsonify({'status': status, 'dataList': topic.get_topic_list(page)})
