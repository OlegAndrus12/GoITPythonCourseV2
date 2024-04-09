# # Binary addition
# binary_num1 = "1010"  # 10
# binary_num2 = "1101"  # 13
# result = bin(int(binary_num1, 2) + int(binary_num2, 2))
# print(result)

# # Binary subtraction
# binary_num1 = "1101"
# binary_num2 = "1010"
# result = bin(int(binary_num1, 2) - int(binary_num2, 2))
# print(result)

# # Binary multiplication
# binary_num1 = "1010"
# binary_num2 = "1101"
# result = bin(int(binary_num1, 2) * int(binary_num2, 2))
# print(result)

# Binary division
binary_num1 = "1101"
binary_num2 = "101"
result = bin(int(binary_num1, 2) // int(binary_num2, 2))
print(result)

# Bitwise AND
num1 = 0b1010
num2 = 0b1100
result = num1 & num2
print(bin(result))

# Bitwise OR
num1 = 0b1010
num2 = 0b1100
result = num1 | num2
print(bin(result))

# Bitwise XOR
num1 = 0b110
num2 = 0b111
result = num1 ^ num2
print(bin(result))

# Bitwise NOT
num = 0b1010
result = ~num
print(bin(result))
