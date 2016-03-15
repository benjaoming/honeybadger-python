import json

class StringReprJSONEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            return repr(o)
        except:
            return '[unserializable]'


def filter_dict(data, filter_keys):
    # filter_keys = set(data.keys())
    for key in filter_keys:
        if data.has_key(key):
            data[key] = "[FILTERED]"
    return data
