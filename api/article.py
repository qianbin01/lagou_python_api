import models.article as article
from flask import Blueprint, jsonify, request
import json

article_blue_print = Blueprint('article', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}

article_doc = article.get_articles_count()


@article_blue_print.route('/lists', methods=['GET', 'POST'])
def lists():
    page = request.args.get('page')
    if request.method == 'GET':
        article_doc['index'] = page
        return jsonify(
            {'status': status,
             'pageInfo': article_doc,
             'dataList': article.get_articles_list('', page)
             })
    else:
        data = json.loads(request.get_data())
        return jsonify({'status': status, 'dataList': article.get_articles_list(data.get('topic_id'), page)})


@article_blue_print.route('/single')
def article_singe():
    aid = request.args.get('aid')
    return jsonify({'status': status, 'object': article.get_articles_single(aid)})
