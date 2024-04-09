# https://www.codewars.com/kata/5acbc3b3481ebb23a400007d/train/python
def is_flush(cards):
    res = set()
    for i in cards:
        res.add(i[-1])
    return len(res) == 1
