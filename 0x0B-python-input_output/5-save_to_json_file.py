#!/usr/bin/python3
""" diccionario de python dado """


import json
""" prototype """


def save_to_json_file(my_obj, filename):
    """ devovler string """
    with open (filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
