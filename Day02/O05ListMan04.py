"""
sort - will sort the original list
sorted - will take a copy of the list sorts it and then returns it
"""
print("sort".center(60, "-"))
l1 = [8, 5, 10, 3, 9, 1, 4, 6, 2, 7]
print(f"l1 :{l1}")

# sorting
res_asc = sorted(l1)
res_desc = sorted(l1, reverse=True)

print(f"Ascending order :{res_asc}")
print(f"Descending order :{res_desc}")

print("-" * 60)
l1 = [8, 'zebra', 'apple', 5, 'yellow', 'black', 10, 'white', 'egg',  3, 'violet', 'green', 9, 'pink', 'maroon', 1, 'xray', 'dog',  4, 'fish', 'ultra', 6, 'red', 'safron',  2, 'ten', 'hen', 7, 129, 1450, 29, 275, 2134]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)

print(f"res :{res}")

print("-" * 60)
for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        break

print("-" * 60)
print(res[:i] + sorted(res[i:]))

print("reverse".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")



