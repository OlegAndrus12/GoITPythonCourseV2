import re


# match() searches for matches from the beginning of a string while
# re.search() searches for matches anywhere in the string

# .group to get result
claim = "People love Python."

print(re.search(r"Python", claim))
# => Python

print(re.match(r"Python", claim))
# => None

print(re.search(r"People", claim))
# => People

print(re.match(r"People", claim))
# => People
