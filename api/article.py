import models.article as article
from flask import Blueprint, jsonify, request
import json

article_blue_print = Blueprint('article', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@article_blue_print.route('/lists/<page>', methods=['GET', 'POST'])
def lists(page):
    if request.method == 'GET':
        return jsonify({'status': status, 'dataList': article.get_articles_list('', page)})
    else:
        data = json.loads(request.get_data())
        return jsonify({'status': status, 'dataList': article.get_articles_list(data.get('topic_id'), page)})
