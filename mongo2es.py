from elasticsearch import Elasticsearch
from models import article
import config

es = Elasticsearch(config.ES_HOST, timeout=180)
es.indices.delete(index='qb-lagou', ignore=[400, 404])
for item in article.find():
    item['aid'] = str(item['_id'])
    item.pop('_id')
    es.index(index="qb-lagou",
             doc_type="article",
             id=item['aid'],
             body=item)
