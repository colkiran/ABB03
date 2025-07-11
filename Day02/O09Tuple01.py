
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4.5, 5.2, 6.0, 7 + 2j, 8 - 3j, 'nine', 'ten', 'eleven', True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(1, 6))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
# tuples are immutable
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")
print(type(t1))

print(f"t1[1] :{t1[1]}")
# t1[1] = 100

print("-" * 60)
# print(dir(t1))
t1 = list(range(1, 6))
print(f"t1 :{t1}")
print(type(t1))

l1 = list(t1)
l1.extend([6, 7, 8, 9, 10])
print(f"l1 :{l1}")
print(type(l1))

t1 = tuple(l1)
print(f"t1 :{t1}")
