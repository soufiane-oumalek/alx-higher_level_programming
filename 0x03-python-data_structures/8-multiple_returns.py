#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if len(sentence) == 0:
        my_tuple = (0, None)
        return my_tuple
    else:
        result = (lenght, sentence[0:1])
        return result
