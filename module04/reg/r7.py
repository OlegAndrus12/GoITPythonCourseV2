import re

s = "news/2021/12/31"
pattern = "(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})"

matches = re.finditer(pattern, s)
for match in matches:
    print(match.groupdict())
