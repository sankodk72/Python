# https://www.codewars.com/kata/is-this-my-tail/train/python

def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
    