import time, random

class Dice:
    def __init__(self, sides, color):
        # instance attributes
        self.sides = sides
        self.color = color
    
    def roll(self):
        print(f"The {self.color} {self.sides} dice is rolling...")
        time.sleep(random.randint(2, 5))
        print(f"{self.color} {self.sides} result: {random.randint(1, self.sides)}")


class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def my_name(self):
        print(f"My name is: {self.name}")
    
    def print_data(self):
        print(f"My name is: {self.name}")
        print(f"My email is: {self.email}")
        print(f"My address is: {self.address}")

john = Person(name="John Randal", email="jrandal@gmail.com", address="Dubai")
jana = Person(name="Jana Ross", email="janaross@gmail.com", address="New York")
tyrese = Person(name="Tyrese Stanton", email="tyrese@gmail.com", address="Spain")

john.print_data()
jana.print_data()