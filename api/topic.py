import models.topic as topic
from flask import Blueprint, jsonify, request

topic_blue_print = Blueprint('topic', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}
topic_doc = topic.get_topic_count()


@topic_blue_print.route('/lists')
def lists():
    page = request.args.get('page')
    topic_doc['index'] = page
    return jsonify(
        {'status': status,
         'pageInfo': topic_doc,
         'dataList': topic.get_topic_list(page)
         })


@topic_blue_print.route('/single')
def single_news():
    tid = request.args.get('tid')
    return jsonify({'status': status, 'object': topic.get_single_topic(tid)})
