"""
static
------
int i
i = 100

dynamic
-------
x = 100
after few lines

x = "hello world"

after few lines

x = True
"""
player_count = 11
print("player_count :", player_count)
rating = 8.8
print(rating)
has_won_world_cup = True
print(has_won_world_cup)
team_name = "India"
print(team_name)

# module
# double underscore name  - dunder_name
print(__name__)     # will return __main__

print("-" * 60)
a, b, c = 1, 3.5, 'hello'
print(a, b, c, sep=", ")

print("-" * 60)
a = b = c = True
print(a, b, c, sep=", ")

print("-" * 60)
first_name = "Sachin"
last_name = "Tendulkar"
print("My name is " + first_name + " and I am also known as " + last_name)

# interpolation - we can print the value of a variable inside double quotes

nm1 = "Ooty Apple"
nm2 = "Kanpur Orange"

string = f"Hello {nm1}, hai {nm2}"
print(string)

print(f"{nm1} cost per kilo is {250 + (250 * 0.09)}\n{nm2} cost per kg is {120 + (120 * 0.09)}")

print("-" * 60)
team_name = "Sahara India"
print(team_name)

team_name = "'Sahara India'"
print(team_name)

team_name = '"Sahara India"'
print(team_name)

team_name = '\'Sahara India\''
print(team_name)







