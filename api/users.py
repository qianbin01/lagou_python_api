import models.article as article
from flask import Blueprint, jsonify

article_blue_print = Blueprint('article', __name__)


@article_blue_print.route('/get')
def get():
    return jsonify(article.article_get())
