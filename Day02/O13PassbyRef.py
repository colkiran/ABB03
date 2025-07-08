
def fun(pax):
    print(f"inside - 1 :{pax}")
    pax.extend(['John', 'Kevin'])
    print(f"inside - 2 :{pax}")

stud = ['Joe', 'Jill', 'Jack']

print(f"Before the function call :{stud}")

fun(stud)

print(f"After the function call :{stud}")
