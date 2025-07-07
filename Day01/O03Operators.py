"""
1. Arithmetic Operators
2. Comparison or Relational
3. Logical
4. Bitwise
5. Ternary
"""

print("Arithmetic Operator".center(60, "-"))
print(f"sum :10 + 3 = {10 + 3}")
print(f"sub :10 - 3 = {10 - 3}")
print(f"mul :10 * 3 = {10 * 3}")
print(f"div :10 / 3 = {10 / 3}")
print(f"flr div :10 // 3 = {10 // 3}")
print(f"mod :10 % 3 = {10 % 3}")
print(f"pwr :10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, !=, >=, <=, >, <
a = 10
b = 20
print(f"a == b :{a == b}")
print(f"a != b :{a != b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 1 == 2 :{1 == 1 and 1 == 2}")
print(f"1 == 2 and 1 == 1 :{1 == 2 and 2 == 2}")

# or
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 ==  2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f"1 == 2 or 2 == 2 :{1 == 2  or 2 == 2}")

# not
print(f"not(1 == 2 and 1 == 1) :{not(1 == 2 and 2 == 2)}")
print(f"not(1 == 1 or 2 == 2 :{not(1 == 1 or 2 ==  2)}")
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")  # integer representation of unicode characters
print(f"ord('z' :{ord('z')}")
print(f"ord('A' :{ord('A')}")
print(f"ord('Z' :{ord('Z')}")
print(f"ord('a' :{ord('a')}")

print("Bitwise operators".center(60, "-"))
print(f"5 | 3: {5 | 3}")
print(f"5 & 3: {5 & 3}")
print(f"5 ^ 3: {5 ^ 3}")
print(f"5 << 1: {5 << 1}")
print(f"8 << 1: {8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print("ternary operator".center(60, "-"))
age = 18
print("Eligible" if age > 17 else "Not Eligible")
