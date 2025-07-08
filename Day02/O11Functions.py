
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greeting Mr.{gname} Welcome to the event.......")

# city is called default arg and name is called non default arg
def greetGstCty(gname,  city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")


greet()

print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)

greetGstCty("Rohit")
greetGstCty("Sachin")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# variable length argument

# if the variable is prefixed with a * then the variable can accept more than one value

def prodAll(*numbers):
    print(numbers)
    print(*numbers)         # unpacking and printing
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(prodAll(1, 2, 3, 4, 5))

print("-" * 60)

# variable is prefixed with ** -> kwargs
def extractDet(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)


extractDet(name="Sachin", age=34, runs=120, oppn="Aus")

print("-" * 60)
# functions also return values

def multiplyMe(x, y):
    return x * y

a = 45
b = 22
print(f"The product of {a} and {b} is :{multiplyMe(a, b)}")

print("-" * 60)
# python supports recursive calls - function calling itself

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

x = 5
print(f"The factorial of {x} is :{fact(x)}")



