
print("extend".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.extend([6, 7, 8, 9])
print(f"l1 :{l1}")

l1.extend([10])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
l1 = list(range(10, 51, 10))
print(f"l1 :{l1}")

l1.insert(1, 15)
l1.insert(3, 25)
l1.insert(5, 35)
l1.insert(7, 45)

print(f"l1 :{l1}")
print(len(l1))
l1.insert(15, 150)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
# return the value that was removed from the list

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"l1 :{l1}")

res = l1.pop(2)
print(res)

res = l1.pop(5)
print(res)

res = l1.pop(-1)
print(res)

print(f"l1 :{l1}")

res = l1.pop()      # removes the last element from the list
print(res)

print("remove".center(60, "-"))
l1 = [1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
      1, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
l1 = [1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
      1, 2, 2, 2, 2, 2]

print("-" * 60)
print(f"l1 :{l1}")

print("-" * 60)
l1 = [x for x in l1 if x != 2]
print(f"l1 :{l1}")

# print("-" * 60)
#
# while 2 in l1:
#     l1.remove(2)
#     print(f"l1 without 2s: {l1}")
#
# print(f"l1 :{l1}")