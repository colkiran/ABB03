
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 5.3, 'six', 7.2, 'eight', 'nine', 'ten', 11.5, 12+2j, 13-5j, True, False }
print(f"s2 :{s2}")

print("-" * 60)
s3 = set(range(1, 6))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
# print(dir(s1))
# add values into a set
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

# add, update
s1.add(1)
s1.add(2)
s1.add(1)
s1.add(3)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(4)

print(f"s1 :{s1}")
# update
s1.update([1, 2, 3])
s1.update([3, 4, 5])
s1.update([7, 8, 9])
s1.update([2, 3, 4])
s1.update([4, 5, 6])
s1.update([8, 9, 10])

print(f"s1 :{s1}")
# remove values from a set - pop, remove, discard
print("-" * 60)
# pop
print(f"s1 :{s1}")
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

s1.remove(5)
s1.remove(8)
# s1.remove(1)
print(f"s1 :{s1}")
print("-" * 60)

s1.discard(3)
s1.discard(7)
s1.discard(1)

print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetric difference A :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozen sets - immutable
fs = frozenset([1, 2, 3, 4, 5])
print(f"fs :{fs}")
print(type(fs))

