import pymongo
import config

client = pymongo.MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
db = client[config.MONGO_DB]
db.authenticate(config.MONGO_AUTH_NAME, config.MONGO_AUTH_PASSWORD)
article = db['article']

recruit = db['recruit']
company = db['company']
comment = db['comment']
comment_user = db['comment_user']
likes = db['likes']
topic = db['topic']
news = db['news_36kr']

