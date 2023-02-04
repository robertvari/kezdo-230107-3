class Dice:
    def __init__(self, sides, color):
        self.__sides = sides
        self.__color = color
    
    @property
    def sides(self):
        return self.__sides

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"

dice6 = Dice(6, "white")
dice6.color = "black"
print(dice6.color)