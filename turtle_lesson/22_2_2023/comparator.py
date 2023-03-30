from turtle import Turtle
from shape import Shape
import turtle


class Comparator(Shape):
    def __init__(self, pen: Turtle, first_line, second_line) -> None:
        super().__init__(pen)
        self._first_line = first_line
        self._second_line = second_line
        self._color = "white"

    def Draw(self):
        turtle.penup()
        turtle.goto(-100, -100)
        turtle.pendown()
        turtle.fillcolor(self._color)
        turtle.begin_fill()
        turtle.forward(self._first_line)
        turtle.left(45)
        turtle.forward(self._second_line)
        turtle.left(135)
        turtle.forward(self._first_line)
        turtle.left(45)
        turtle.forward(self._second_line)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-250, -140)
        turtle.pendown()
        label = "Perimeter: " if self._color == "green" else "Area: "
        func = self.get_perimeter() if self._color == "green" else self.get_area()
        turtle.write(f"{label}{func}", font=("Arial", 10, "normal"))

    def get_perimeter(self):
        perimeter = 2*self._first_line + 2*self._second_line
        return perimeter

    def get_area(self):
        area = self._first_line * self._second_line
        return area

    def compare(self):
        if self.get_perimeter() > self.get_area():
            self._color = "green"
        elif self.get_perimeter() < self.get_area():
            self._color = "blue"
        else:
            self._color = "red"
