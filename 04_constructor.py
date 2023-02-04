class Dice:
    def __init__(self, sides, color):
        # instance attributes
        self.sides = sides
        self.color = color


dice6 = Dice(sides=6, color="Blue")
dice10 = Dice(sides=10, color="Red")
dice20 = Dice(sides=20, color="Green")

print(dice6.color, dice6.sides)
print(dice10.color, dice10.sides)
print(dice20.color, dice20.sides)