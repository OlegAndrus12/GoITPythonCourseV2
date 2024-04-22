import re

target_string = "The price of PINEAPPLE ice cream is 20"

# two groups enclosed in separate ( and ) bracket
result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)

# Extract matching values of all groups
print(result.groups())
# Output ('PINEAPPLE', '20')

# Extract match value of group 1
print(result.group(1))
# Output 'PINEAPPLE'

# Extract match value of group 2
print(result.group(2))
# Output 20
