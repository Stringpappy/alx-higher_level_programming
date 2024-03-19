#!/usr/bin/python3
def multiple_returns(sentence):
    j = len(sentence)
    if j == 0:
        return 0, None
    if j > 0:
        return j, sentence[0]
