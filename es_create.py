from elasticsearch import Elasticsearch
import sys
doc_fetch_all= {
    'size' : 10000,
    'query': {
        'match_all' : {}
    }
}

class ES_ModelHelper:

    def __init__(self,client_name):
        self._es_host = {"host": "localhost", "port": 9200}
        self._es = Elasticsearch(hosts=[self._es_host])
        self._client_name = client_name


    def create_word_index_map(self):
        return_json = {}
        return_json["message"] = ""
        return_json["result"] = ""
        try:
            index_name = "index_" + self._client_name
            if self._es.exists(index=index_name,doc_type='client_info', id="word_corpus_"+ self._client_name):
                print("y")
                self._es.delete(index=index_name, doc_type="client_info",id="word_corpus_" + self._client_name)
            res = self._es.search(index=index_name, doc_type="client_info", body=doc_fetch_all)
            print("res", res)
            word_index_map = []
            for hit in res['hits']['hits']:
                if "_source" in hit and len(hit["_source"])!=0 and "word_idf_score" in hit["_source"] and len(hit["_source"]["word_idf_score"])!=0:
                    word_list = hit["_source"]["word_idf_score"][0].keys()
                    for i in set(word_list):
                        word_index_map.append(i)
                else:
                    continue
            print("qqqq",word_index_map)
            print("ssss",list(set(word_index_map)))
            doc_json = {}
            doc_json["word_index_map"] = list(set(word_index_map))
            print(doc_json)
            self._es.index(index=index_name, doc_type='client_info', id="word_corpus_" +self._client_name, body=doc_json)
        except Exception as e:
            return_json["message"] = "System has encountered an error."
            print(e)
            print('Error on line {}{}{}'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
        print(return_json)

    def update_word_index_map(self):
        return_json = {}
        return_json["message"] = ""
        return_json["result"] = ""
        try:
            index_name = "index_" + self._client_name
            res = self._es.get(index=index_name, doc_type='client_info', id="5cadd8be41ff7a7190beebcd")
            new_wl = list(res["_source"]["word_idf_score"][0].keys())
            print(new_wl)
            if self._es.exists(index=index_name, doc_type='client_info', id="word_corpus_" + self._client_name):
                res = self._es.get(index=index_name, doc_type='client_info', id="word_corpus_" + self._client_name)
            print(res)
            word_list = list(res["_source"]["word_index_map"])
            print(word_list,len(word_list))
            word_index_map=set(word_list+new_wl)
            print(word_index_map, len(word_index_map))
            doc_json = {}
            doc_json["word_index_map"] = list(word_index_map)
            self._es.update(index=index_name, doc_type='client_info', id="word_corpus_" + self._client_name, body={"doc":doc_json})
        except Exception as ex:
            return_json["message"] = "System has encountered an error."
            print(ex)
        return return_json

    def get_word_index_map(self):
        return_json = {}
        return_json["message"] = ""
        return_json["result"] = ""
        word_index_map =[]
        try:
            index_name = "index_" + self._client_name
            res = self._es.get(index=index_name+"_corpus", doc_type='client_info', id="word_corpus" + self._client_name)
            # print(res.status)
            # res.
            # if res.status ==200:
            print(res)

            word_index_map = res["_source"]["word_index_map"]

        except Exception as ex:
            print( '{} {} {}'.format(sys.exc_info()[-1].tb_lineno,type(ex).__name__, ex ))
            return_json["message"] = "word index map is not present"
        return word_index_map


es= ES_ModelHelper("xxxx_doc")
# es.create_word_index_map()
# es.update_word_index_map()
print(es.get_word_index_map())