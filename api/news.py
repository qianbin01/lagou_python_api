import models.news as news
from flask import Blueprint, jsonify

news_blue_print = Blueprint('news', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}


@news_blue_print.route('/lists/<page>')
def lists(page):
    return jsonify({'status': status, 'dataList': news.get_news_list(page)})


@news_blue_print.route('/single/<nid>')
def single_news(nid):
    return jsonify({'status': status, 'object': news.get_single_news(nid)})
