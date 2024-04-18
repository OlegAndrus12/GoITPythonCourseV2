def camel_to_snake(str):
    j = 0
    res = ""
    for i in str:
        if i.isupper():
            if j == 0:
                res += i.lower()
            else:
                res += "_" + i.lower()
        else:
            res += i
        j += 1
    return res


# Driver code
str = "GeeksForGeeks"
print(camel_to_snake(str))
