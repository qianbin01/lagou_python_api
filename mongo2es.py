from elasticsearch import Elasticsearch
from models import recruit
import config

es = Elasticsearch(config.ES_HOST, timeout=180)
es.indices.delete(index='qb-lagou', ignore=[400, 404])
for item in recruit.find():
    item['rid'] = str(item['_id'])
    item.pop('_id')
    es.index(index="qb-lagou",
             doc_type="recruit",
             id=item['rid'],
             body=item)
