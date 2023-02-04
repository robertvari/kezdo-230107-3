class Dice:
    def __init__(self, sides, color):
        self.__sides = sides
        self.__color = color

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"

dice6 = Dice(6, "white")
print(dice6)