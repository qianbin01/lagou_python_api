from elasticsearch import Elasticsearch
import config

es = Elasticsearch(config.ES_HOST, timeout=180)


def search_from_es(doc_type, page, **kwargs):
    body = {
        "query": {
            "match_all": {}
        },
        "from": 10 * (page - 1),
        "size": 10,
    }
    if kwargs:
        must = [{"match_phrase": {item: kwargs[item]}} for item in kwargs]
        body = {
            "query": {
                "bool": {
                    "must": must
                },
            },
            "from": 10 * (page - 1),
            "size": 10,
        }
    res = es.search(index='qb-lagou', doc_type=doc_type, body=body)
    return res['hits']
