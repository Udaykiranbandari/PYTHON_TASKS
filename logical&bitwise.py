# Logical AND (and)
a = True
b = False
print("Logical AND:", a and b)  # Output: False (since one value is False)

# Logical OR (or)
x = 5
y = 10
print("Logical OR:", x > 2 or y < 5)  # Output: True (since x > 2 is True)

# Logical NOT (not)
flag = True
print("Logical NOT:", not flag)  # Output: False (inverts True to False)


# Bitwise AND (&)
a = 5  # 0101 (binary)
b = 3  # 0011 (binary)
print("Bitwise AND:", a & b)  # Output: 1 (0001 in binary)

# Bitwise OR (|)
a = 5  # 0101 (binary)
b = 3  # 0011 (binary)
print("Bitwise OR:", a | b)  # Output: 7 (0111 in binary)

# Bitwise XOR (^)
a = 5  # 0101 (binary)
b = 3  # 0011 (binary)
print("Bitwise XOR:", a ^ b)  # Output: 6 (0110 in binary)

# Bitwise NOT (~)
a = 5  # 0101 (binary)
print("Bitwise NOT:", ~a)  # Output: -6 (inverts bits, 2's complement)

# Bitwise Left Shift (<<)
a = 5  # 0101 (binary)
print("Left Shift:", a << 1)  # Output: 10 (1010 in binary, shifts left)

# Bitwise Right Shift (>>)
a = 5  # 0101 (binary)
print("Right Shift:", a >> 1)  # Output: 2 (0010 in binary, shifts right)


# Logical Operators Example
a = 10
b = 5

print("Logical AND:", (a > 5 and b < 10))  # True and True → True
print("Logical OR:", (a < 5 or b < 10))    # False or True → True
print("Logical NOT:", not(a > b))          # not(True) → False


# Bitwise AND, OR, XOR Example
a = 6  # 0110 in binary
b = 3  # 0011 in binary

print("Bitwise AND:", a & b)  # 0110 & 0011 → 0010 (2)
print("Bitwise OR:", a | b)   # 0110 | 0011 → 0111 (7)
print("Bitwise XOR:", a ^ b)  # 0110 ^ 0011 → 0101 (5)


# Bitwise NOT, Left Shift, and Right Shift Example
x = 5  # 0101 in binary

print("Bitwise NOT:", ~x)     # ~0101 → -6 (Two’s complement)
print("Left Shift:", x << 2)  # 0101 << 2 → 10100 (20)
print("Right Shift:", x >> 1) # 0101 >> 1 → 0010 (2)

