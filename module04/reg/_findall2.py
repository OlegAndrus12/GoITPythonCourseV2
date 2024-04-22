import re 


def solve(s):
    return max(re.findall(r"[aeiou]+", s), key=len, default="")

print(solve("asdasdasdasdssssssaaaaas"))