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


@article_blue_print.route('/single/<aid>')
def article_singe(aid):
    return jsonify({'status': status, 'object': article.get_articles_single(aid)})


@article_blue_print.route('/comments/<aid>')
def article_comments(aid):
    return jsonify({'status': status, 'dataList': article.get_article_comments(aid)})


@article_blue_print.route('/comments/user/<cid>')
def article_comment_user(cid):
    return jsonify({'status': status, 'object': article.get_article_comment_user(cid)})
