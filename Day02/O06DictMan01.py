
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)

d2 = {'name': 'sachin', 'age': 35, 'runs': 89, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)

d3 = dict([('name', 'Rahul'), ('age', 32), ('runs', 45), ('oppn', 'Nzl')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Virat', age=30, runs=120, oppn="Eng")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
# create
player = {'name': 'Sachin', 'age': 38, 'runs': 98, 'oppn': 'WI'}
print(f"player :{player}")

# Read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for x in player:
    print(x, "=>", player[x])

# update - modify, add a new key value pairs

# modify
player['name'] = "Tendulkar"
player['runs'] = 145

print(f"player :{player}")

# add new key value
player['venue'] = 'Sabina Park'
player['year'] = '2009'

print(f"player :{player}")

# del
del player['age']
del player['oppn']

print(f"player :{player}")

# print("-" * 60)
# print(dir(player))

print("keys".center(60, "-"))
emp = {'empid': 'EMP111', 'ename': 'Ruben', 'age': 35, 'desig': 'MGR', 'dept': 'MKT', 'salary': 85000}
print(f"emp :{emp}")

k = emp.keys()
print(f"keys :{k}")

print("-" * 60)
for k in emp.keys():
    print(k + " => " + str(emp[k]))

print("values".center(60, "-"))
emp = {'empid': 'EMP111', 'ename': 'Ruben', 'age': 35, 'desig': 'MGR', 'dept': 'MKT', 'salary': 85000}
print(f"emp :{emp}")

v = emp.values()
print(f"v :{v}")
