# coding=utf-8

"""
FileName: params.py
Author: ken
Date: 2018-03-19
Describe: params ex
"""
import json


def print_params(**params):
    return params


def print_params_2(x, y, z=3, *pospar, **keypar):
    return x, y, z, pospar, keypar


def json_format(result):
    value = json.dumps(result, indent=4)
    return value


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


if __name__ == "__main__":
    # print(json_format(print_params(x=1, y=2)))
    # print(print_params_2(1, 2, 3, 5, 6, 7, fool=1, bar=2))
    d = {}
    init(d)
    store(d, 'Han Solo')
    print(lookup(d, 'first', 'Han'))
