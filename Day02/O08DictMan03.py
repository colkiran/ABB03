
print("items".center(60, "-"))
# items  -> keys() + values()

emp = {
    'emp1' :{'empid': 'EMP101', 'ename': 'Grace', 'age': 30, 'desig': 'TL', 'dept': 'Finance', 'Salary': 85000},
    'emp2' :{'empid': 'EMP220', 'ename': 'Mike', 'age': 35, 'desig': 'MGR', 'dept': 'MKT', 'Salary': 125000},
    'emp3' :{'empid': 'EMP333', 'ename': 'Slater', 'age': 37, 'desig': 'PM', 'dept': 'IT', 'Salary': 235000}
}

print(f"emp :{emp}")

print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print("-" * 60)

print(f"emp2 :{emp['emp2']}")
print("-" * 60)

print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("update".center(60, "-"))
emp1 = {'empid': 'EMP101', 'ename': 'Grace', 'age': 30, 'desig': 'TL', 'Salary': 85000}

emp2 = {'empid': 'EMP220', 'ename': 'Mike', 'age': 35, 'desig': 'MGR', 'dept': 'MKT'}

print(f"emp1 :{emp1}")

print("-" * 60)
print(f"emp2 :{emp2}")

print("-" * 60)
emp1.update(emp2)

print(f"emp1 :{emp1}")

print('copy'.center(60, "-"))
d1 = {'name': 'sachin', 'age': 32, 'runs': 80}
print(f"d1 before :{d1}")

# copy the dictionary d1 to d2
d2 = d1         # shallow copy - copies the data and address
print(f"d2 before :{d2}")

d2['oppn'] = 'Zim'
d2['venue'] = 'Chinnaswamy'

print("-" * 60)
print(f"d2 after :{d2}")
print("-" * 60)
print(f"d1 after :{d1}")

print("=" * 60)
print("=" * 60)

d3 = {'empid': 110, 'ename': 'Jack', 'age': 25}
print(f"d3 before :{d3}")

# copy dictionary d3 to d4
d4 = d3.copy()
print(f"d4 before :{d4}")

d4['dept'] = 'MKT'
d4['desig'] = 'BDE'

print(f"d3 after :{d3}")
print(f"d4 after :{d4}")

print("=" * 60)
print("=" * 60)

d5 = {'studid': 151, 'sname': 'Peter', 'age': 14, 'marks': {'maths': 67, 'science': 75, 'social': 60}}
print(f"d5 before :{d5}")

d6 = d5.copy()      # deep copy
print(f"d6 before :{d6}")

d6['marks']['lan1'] = 80
d6['marks']['lan2'] = 58

print("-" * 60)
print(f"d6 after :{d6}")

print("-" * 60)
print(f"d5 after :{d5}")

print("=" * 60)
print("=" * 60)

d7 = {'studid': 151, 'sname': 'Peter', 'age': 14, 'marks': {'maths': 67, 'science': 75, 'social': 60}}

print(f"d7 :{d7}")

from copy import deepcopy
d8 = deepcopy(d7)

print(f"d8 before :{d8}")

d8['marks']['lan1'] = 55
d8['marks']['lan2'] = 62

print(f"d8 after :{d8}")
print(f"d7 after :{d7}")