
class Player:           # pascal casing

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 45)
ply1.get_details()

print("-" * 60)
ply2 = Player("Virat", 36)
ply2.get_details()

print("-" * 60)
print(f"isinstance(ply1, Player) :{isinstance(ply1, Player)}")
print(f"isinstance(ply1, object) :{isinstance(ply1, object)}")
