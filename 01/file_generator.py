def file_filter(file, search_words: list) -> str:
    lower_search_words = set(s.lower() for s in search_words)
    with open(file, "r", encoding="utf-8") as file_obj:
        for data in file_obj:
            data_lower_list = data.lower().split()
            for elem in data_lower_list:
                if elem in lower_search_words:
                    yield data
                    break
