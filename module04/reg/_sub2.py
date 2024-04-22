import re

# multiline string
string = "abc 12\
de 23 \n   \tf45 6"

# matches all whitespace characters
pattern = "\s+"

# empty string
replace = ""

new_string = re.sub(pattern, replace, string)
print(new_string)


new_string = re.subn(pattern, replace, string)
print(new_string)
