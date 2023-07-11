#!/usr/bin/python3
""" Class Student to JSON"""


class Student:
    """declare class student"""

    def __init__(self, first_name, last_name, age):
        """intiliaze a student
        Args:
        @first_name: the first name of student
        @last_name: the last name of student
        @age: the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            try:
                dic[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
            return dic

    def reload_from_json(self, json):
        """retrieves a dictionary representation of a Student"""

        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
