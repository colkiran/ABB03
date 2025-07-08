
print("Maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'

# the length of a and b should be the same

restbl = st.maketrans(a, b)
print(f"restbl :{restbl}")

print("translate".center(60, "-"))
res = st.translate(restbl)
print(f"res :{res}")

print("-" * 60)
st = "122334243Micheal452332346"
print(f"st :{st}")
# extract the name from the string

for i in range(0, len(st)):
    if st[i].isalpha():
        print(st[i], end=" ")
print()

res = " ".join([i for i in st if i.isalpha()])   # comprehension
print(res)

print("format".center(60, "-"))
print("Hi {}, what a {} player".format("Sachin", "class"))
print("Hi {nm} with a rating of {rat:.3f} for {cntry}".format(nm="Sachin", rat = 4.633434, cntry="India"))
print("Hi {0} what a {1} player for {2}".format("Sachin", "class", "India"))

