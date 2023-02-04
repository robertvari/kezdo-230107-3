class Dice:
    # class attribute
    sides = 100
    color = "yellow"

    def __init__(self, sides, color):
        # instance attributes
        self.sides = sides
        self.color = color

class Person:
    # class attribute always the same for each instance
    race = "human"

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

robert = Person(name="Robert", age=30, address="Budapest")
csaba = Person(name="Csaba", age=24, address="Pécs")
Kriszta = Person(name="Kriszta", age=22, address="Debrecen")

print(robert.name, robert.age, robert.address)
print(csaba.name, csaba.age, csaba.address)
print(Kriszta.name, Kriszta.age, Kriszta.address)
print(Person.race)
Person.race = "monkey"

print(robert.race)
print(csaba.race)
print(Kriszta.race)