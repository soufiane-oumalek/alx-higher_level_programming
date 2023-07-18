#!/usr/bin/python3
"""imports modules"""
import json
import os.path
import csv


class Base:
    """intialize class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """objects in file"""
        filename = "{}.json".format(cls.__name__)
        l_dics = []

        if not list_objs:
            pass
        else:
            for index in range(len(list_objs)):
                l_dics.append(list_objs[index].to_dictionary())
        lists = cls.to_json_string(l_dics)

        with open(filename, "w") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """that returns the JSON string
        representation of list_dictionaries"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_dic = cls(10, 10)
        else:
            new_dic = (10)
        new_dic.update(**dictionary)
        return new_dic
