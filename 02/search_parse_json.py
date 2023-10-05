import json


def words_callback(word):
    pass


def parse_json(json_str: str, keyword_callback, required_fields=None,  keywords=None):
    json_doc = json.loads(json_str)
    count = 0
    for key in json_doc.keys():
        if key in required_fields:
            for word in json_doc[key].lower().split():
                if word in keywords:
                    words_callback(word)




