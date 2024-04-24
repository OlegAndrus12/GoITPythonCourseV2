message = "Hello world!"
print(message.encode())  # UTF-8
print(message.encode("utf-16"))
print(message.encode("cp1251"))

#  Save binary
with open("utf-8.txt", "wb") as f:
    f.write(message.encode())

with open("utf-16.txt", "wb") as f:
    f.write(message.encode("utf-16"))

with open("cp1251.txt", "wb") as f:
    f.write(message.encode("cp1251"))

#  Read
with open("utf-8.txt", "rb") as f:
    print(f.read().decode())

with open("utf-16.txt", "rb") as f:
    print(f.read().decode("utf-16"))

with open("cp1251.txt", "rb") as f:
    print(f.read().decode("cp1251"))
