# https://www.codewars.com/kata/55b4f9906ac454650900007d/train/python
def string_chunk(st, n):
    res = list()
    for i in range(0, len(st), n):
        res.append(st[i : i + n])
    return res
