import models.news as news
from flask import Blueprint, jsonify, request

news_blue_print = Blueprint('news', __name__)
status = {
    'msg': '请求成功',
    'code': 1000
}
news_doc = news.get_news_count()


@news_blue_print.route('/lists')
def lists():
    page = request.args.get('page')
    news_doc['index'] = page
    return jsonify(
        {'status': status,
         'pageInfo': news_doc,
         'dataList': news.get_news_list(page)
         })


@news_blue_print.route('/single')
def single_news():
    nid = request.args.get('nid')
    return jsonify({'status': status, 'object': news.get_single_news(nid)})
