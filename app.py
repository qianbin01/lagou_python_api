from flask import Flask
from api import article, company, recruit, topic, comment, news, users

app = Flask(__name__)
app.register_blueprint(article.article_blue_print, url_prefix='/article')
app.register_blueprint(company.company_blue_print, url_prefix='/company')
app.register_blueprint(recruit.recruit_blue_print, url_prefix='/recruit')
app.register_blueprint(topic.topic_blue_print, url_prefix='/topic')
app.register_blueprint(news.news_blue_print, url_prefix='/news')
app.register_blueprint(comment.comment_blue_print, url_prefix='/comment')
app.register_blueprint(users.comment_user_blue_print, url_prefix='/comment_users')

if __name__ == '__main__':
    app.run(debug=True)
