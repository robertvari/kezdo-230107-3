class Dice:
    def __init__(self, sides, color):
        # access level: Public
        self.color = color

        # access level: Private
        self.__sides = sides
    
    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.color}"
    
dice6 = Dice(6, "white")
print(dice6)

dice6.color = "Red"
print(dice6)

dice6.__sides = 100000 
dice6.name = "Robert"
print(dice6)