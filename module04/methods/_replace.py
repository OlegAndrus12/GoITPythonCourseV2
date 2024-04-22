# https://www.codewars.com/kata/56a24b309f3671608b00003a/python
def dad_filter(string):
    while ",," in string:
        string = string.replace(",,", ",")
    return string.strip(", ")


res = dad_filter("asdsad,d,as,dsa,dsa,das,d,,,asdsad ,,,asd,,")
print(res)
