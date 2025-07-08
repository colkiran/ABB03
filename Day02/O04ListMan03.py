
print("clear".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("count".center(60, "-"))
l1 = [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2,2, 2, 2, 1, 2, 3, 1, 1, 1,1,
      1, 2, 1, 2, 2, 2]

print(f"l1 :{l1}")

print("-" * 60)
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")

print("index".center(60, "-"))

l1 = [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1,1,
      1, 2, 1, 2, 2, 2]

print(f"l1 :{l1}")

print("-" * 60)
print(f"first 3 :{l1.index(3)}")
print(f"second 3 :{l1.index(3, l1.index(3) + 1)}")
print(f"third 3 :{l1.index(3, l1.index(3, l1.index(3) + 1) + 1)}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the elements of l1 into l2
l2 = l1         # shallow copy  - we copy the data with the address

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
print("=" * 60)

l3 = [6, 7, 8, 9, 10]
print(f"l3 :{l3}")

# copy the elements of l3 to l4
l4 = l3.copy()          # deep copy - only data is shared

print(f"l4 before :{l4}")

l4.extend([11, 12, 13])

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
print("=" * 60)

l5 = [1, 2, 3, [2, 4, 6, 8, 10], 4, 5]
print(f"l5 before :{l5}")

# copy the elements of l5 to l6

l6 = l5.copy()

l6[3].extend([12, 13, 14])

print(f"l5 after :{l5}")
print(f"l6 after :{l6}")

print("=" * 60)
print("=" * 60)
l7 = [1, 3, 5, 7, [2, 4, 6, 8],  9]
print(f"l7 before :{l7}")

# copy the elements of l7 into l8
from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")
l8[4].extend([10, 12, 14, 16])

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")