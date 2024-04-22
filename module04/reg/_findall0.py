import re

# Sample text
sample_text = "Alice lives in 1230 First St., Ocean City, MD 156789."

# Create a regular expression object with the regular expression '\d' {4}
regex = re.compile(r"\d+")

# Search the sample_text for the regular expression
matches = re.findall(regex, sample_text)

# Print all the matches
for match in matches:
    print(match)
