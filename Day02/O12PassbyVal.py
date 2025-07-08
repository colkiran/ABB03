
def fun(x):
    print(f"x inside - 1:{x}")
    x += 10
    print(f"x inside - 2 :{x}")
    
y = 5

print(f"Before the function call :{y}")

fun(y)

print(f"After the function call :{y}")