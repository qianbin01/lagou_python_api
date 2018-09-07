from elasticsearch import Elasticsearch
import config

es = Elasticsearch(config.ES_HOST, timeout=180)


def search_from_es(doc_type, body=None, index='qb-lagou'):
    if not body:
        body = {"match_all": {}}
    res = es.search(index=index, doc_type=doc_type, body={"query": body})
    return res['hits']['hits']
