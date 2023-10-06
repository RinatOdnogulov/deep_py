import json


def words_callback(word):
    pass


def parse_json(json_str: str, keyword_callback, required_fields=None,  keywords=None):
    print(json_str)
    json_doc = json.loads(json_str)
    print(json_doc)
    for key in json_doc.keys():
        if key in required_fields:
            for word in json_doc[key].lower().split():
                if word in keywords:
                    keyword_callback(word)


json_str = '{"key1": "Word1 Word2 word2", "key2": "word2 word3"}'
required_fields = ["key1"]
keywords = ["word2"]


parse_json(json_str, words_callback, required_fields, keywords)