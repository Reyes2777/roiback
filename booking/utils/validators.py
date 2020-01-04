from unicodedata import normalize


def is_valid_queryparam(param):
    return param != '' and param is not None


def normalize_string(string):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    return normalize('NFKC', normalize('NFKD', string).translate(trans_tab))
