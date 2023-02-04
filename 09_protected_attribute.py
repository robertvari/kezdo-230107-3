class Dice:
    def __init__(self, sides, color):
        # access level: Public
        self.color = color

        # access level: Protected
        self._sides = sides
    
    def __str__(self) -> str:
        return f"Sides: {self._sides} Color: {self.color}"

dice6 = Dice(6, "white")
print(dice6)

# only print, not override!!!
dice6._sides = 10
# dice6.color = "red"
print(dice6._sides)