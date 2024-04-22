def formatted_numbers():
    res = list()
    header = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
    res.append(header)
    for i in range(16):
        res.append(f"|{i:=<10d}|{i:*^10x}|{i:h>10b}|")
    return res


for el in formatted_numbers():
    print(el)