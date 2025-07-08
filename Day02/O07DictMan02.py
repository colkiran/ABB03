
print("get".center(60, "-"))
emp = {'empid': 'EMP111', 'ename': 'Ruben', 'age': 35, 'desig': 'MGR', 'dept': 'MKT', 'salary': 85000}

print(f"emp :{emp}")

print("-" * 60)
print(f"Name  :{emp.get('ename', 'Invalid key, Please enter a valid key.....')}")
print(f"Desig :{emp.get('desg', 'Invalid key, Please enter a valid key.....')}")

print("from_keys".center(60, "-"))
cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f'res1 :{res1}')

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("setdefault".center(60, "-"))
player = {'name': 'Sourav', 'age': 35, 'runs': 100}
print(f"player: {player}")

print("-" * 60)

player.setdefault('name', 'Ganguly')
player.setdefault('runs', 65)
player.setdefault('oppn', 'SA')
player.setdefault('venue', 'Chepauk')

print(f"player: {player}")

print("pop".center(60, "-"))
player = {'name': 'Sourav', 'age': 35, 'runs': 100, 'oppn': 'SA', 'venue': 'Chepauk'}

print(f"player :{player}")

print("-" * 60)
res = player.pop('age')
print(res)

res = player.pop('venue')
print(res)

# res = player.pop()
# print(res)

print(f"player :{player}")

print("popitem".center(60, "-"))

player = {'name': 'Sourav', 'age': 35, 'runs': 100, 'oppn': 'SA', 'venue': 'Chepauk'}

print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player: {player}")

