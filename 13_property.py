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

class Student:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__marks = []

    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def student_marks(self):
        return self.__marks

    @property
    def avarage(self):
        return sum(self.__marks) / len(self.__marks)

    def add_mark(self, value):
        self.__marks.append(value)

    def __repr__(self):
        return f"{self.__first_name} {self.__last_name}"

stevie = Student("Stevie", "Powers")
print(stevie)
stevie.add_mark(1)
stevie.add_mark(3)
stevie.add_mark(2)
stevie.add_mark(2)
stevie.add_mark(1)
stevie.add_mark(1)
print(stevie.student_marks)
print(stevie.avarage)