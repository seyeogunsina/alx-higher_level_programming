#!/usr/bin/python3
def multiple_returns(sentence):
    res = (len(sentence) if sentence else None, sentence[0])
    return res
