
from re import compile, sub

REGEX = compile(r",+")


def dad_filter(strng):
    return sub(REGEX, ",", strng).rstrip(" ,")


res = dad_filter("asdsad,d,as,dsa,dsa,das,d,,,asdsad ,,,asd,,")
print(res)
