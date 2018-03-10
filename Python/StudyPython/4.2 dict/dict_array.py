# coding=utf-8
import json


def json_format(data):
    j_format = json.dumps(data, ensure_ascii=False, indent=4, default=None)
    return j_format


if __name__ == "__main__":
    di = {"Alice": {"phone": "9012", "address": "Foo drive 23"}}
    print json_format(di)
