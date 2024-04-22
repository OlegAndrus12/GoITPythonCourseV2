import re

text = (
    "Ima.Fool@iana.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com "
    "abc111@test.com.net 12Fool1@iana.org"
)


# Найти email
result = re.findall(r"\b[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
print(result)

# Найти домен
result = re.findall(r"\b[a-zA-Z]{1}[\w\.]+@([a-zA-Z]+\.[a-zA-Z]{2,})", text)
print(result)
