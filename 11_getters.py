class Dice:
    def __init__(self, sides, color):
        # access level: Public
        self.color = color

        # access level: Private
        self.__sides = sides
    
    def get_sides(self):
        return self.__sides

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.color}"


dice6 = Dice(6, "white")
print(dice6.get_sides())
print(dice6.color)