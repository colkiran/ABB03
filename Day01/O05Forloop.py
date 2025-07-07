"""
1. continue - skip the current iteration
2. break - stop the current iteration
3. else
"""
for i in range(1, 11):
    print(i, end=" ")
print()         # new line

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 31):
    # if i > 24:
    #     break
    if i % 2 == 0:
        continue
    print(i, end=" ")
else:
    print("\nCompleted generating numbers.....")

