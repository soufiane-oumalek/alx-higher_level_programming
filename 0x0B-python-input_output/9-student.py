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


def to_json(self):
    return self.__dict__
