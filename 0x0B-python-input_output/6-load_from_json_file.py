#!/usr/bin/python3
""" diccionario de python dado """


import json
""" prototype """


def load_from_json_file(filename):
    """ devovler string """
    with open(filename, encoding="utf-8") as f:
        return(json.loads(f.read()))
