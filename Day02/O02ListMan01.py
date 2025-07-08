
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.2, 6.0, 7.1, 8.9, 'nine', 'ten', 'eleven', 'twelve', 13 + 2j, 14 - 3j, True, False]
print(f"l2 :{l2}")
print(type(l2))
print(id(l2))

print("-" * 60)
l3 = list(range(10, 101, 10))
print(f'l3 :{l3}')
print(type(l3))

print("-" * 60)
# CRUD List

# create a list
studs = ['John', 'Jack', 'Kevin', 'Tina', 'Mike']
print(f"studs :{studs}")

# read
print(f"studs[1] :{studs[1]}")
print(f"studs[-1] :{studs[-1]}")

for i in studs:
    print(i, end=" ")
print()

# update - replace, add a new name
# replace
print(f"studs :{studs}")

studs[0] = 'Martin'
studs[3] = 'Richard'

# mutable
print(f"studs :{studs}")

# add a new name (static not supported)
studs[3] = "Peter"
print(f"studs :{studs}")
print(id(studs))
# delete
del studs[2]
del studs[-1]

print(f"studs :{studs}")
print(id(studs))

# print("-" * 60)
# print(dir(studs))
print('append'.center(60, "-"))

l1 = [1, 2, 3, 4, 5]
print(f"l1: {l1}")
print(id(l1))

# can one element at a time
l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")
print(id(l1))

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

# print 10, 11 and 12
print(f"l1[8][1:4] :{l1[8][1:4]}")
