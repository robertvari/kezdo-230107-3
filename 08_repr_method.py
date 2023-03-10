class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self) -> str:
        return f"My name is {self.name}. My email: {self.email}. I live in {self.address}"
    
    def __repr__(self) -> str:
        return self.name

robert = Person("Robert", "robert@gmail.com", "Budapest")
csaba = Person("Csaba", "csaba@gmail.com", "Debrecen")
kriszta = Person("Kriszta", "kriszta@gmail.com", "Pécs")

my_friends = [robert, csaba, kriszta]
print(my_friends[1])
print(my_friends)