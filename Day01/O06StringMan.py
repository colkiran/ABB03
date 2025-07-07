
st = "hello world"
print(f"st :{st}")
print(type(st))

print(f"st[0] :{st[0]}")        # strings are stored like arrays (indexed)
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
# check for palindrome
st = "malayalam"
print(f"Palindrome - {st[:]}" if st[:] == st[::-1] else f"Not a Palindrome - {st[:]}")

print("-" * 60)
st = "hello"
print(f'st :{st}')
print(st[0])
# st[0] = "H"

print("-" * 60)
st = "hello world"

# replace
res = st.replace("w", "W")
print(f"res :{res}")

print("-" * 60)
res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 60)
print(dir(st))
