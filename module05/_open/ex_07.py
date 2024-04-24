res = ""
with open("test.txt", "r") as f:
    res += f.read(13)
    print(f.tell())
    f.seek(0)
    print(f.tell())
    res += f.read(13)
    print(f.tell())
    res += f.read(10)
    res += f.read(10)


print(res)
