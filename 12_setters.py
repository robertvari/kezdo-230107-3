class Dice:
    allowed_sides = [6, 10, 20]
    allowed_colors = ["white", "red", "green", "blue"]

    def __init__(self, sides, color):
        self.__check_sides(sides)
        self.__check_color(color)

        # access level: Public
        self.__color = color

        # access level: Private
        self.__sides = sides
    
    def get_sides(self):
        return self.__sides

    def set_sides(self, new_sides):
        assert isinstance(new_sides, int), "Sides must be of type int!"
        self.__check_sides(new_sides)

        self.__sides = new_sides

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__check_color(new_color)
        self.__color = new_color

    # private method starts with: __
    def __check_sides(self, sides):
        assert sides in self.allowed_sides, f"Allowed Sides: {self.allowed_sides}"

    def __check_color(self, color):
        assert color in self.allowed_colors, f"Allowed colors: {self.allowed_colors}"

    def __str__(self) -> str:
        return f"Sides: {self.__sides} Color: {self.__color}"

dice6 = Dice(6, "green")
print(dice6)
dice6.set_sides(10)
print(dice6)
dice6.set_color("blue")
print(dice6)