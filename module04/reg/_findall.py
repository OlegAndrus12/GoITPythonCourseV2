import re

# Sample text
sample_text = "Bot activity detected: 192.16.4.162, 69.168.21.343 looks suspicios"

# Create a regular expression object with the regular expression '\d'
regex = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

# Search the sample_text for the regular expression
matches = re.findall(regex, sample_text)

# Print all the matches
for match in matches:
    print(match)
