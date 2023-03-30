from turtle import Turtle
from shape import Shape
import turtle
from math import pi



class Circle(Shape):
    def __init__(self, pen: Turtle, radius) -> None:
        super().__init__(pen)
        self._radius = radius
        self._color = "white"

    def Draw(self):
        turtle.penup()
        turtle.goto(-200, 200)
        turtle.left(45)
        turtle.pendown()
        turtle.fillcolor(self._color)
        turtle.begin_fill()
        turtle.circle(self._radius)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-270, 200)
        turtle.pendown()
        label = "Perimeter: " if self._color == "green" else "Area: "
        func = self.get_perimeter() if self._color == "green" else self.get_area()
        turtle.write(f"{label}{int(func)}", font=("Arial", 10, "normal"))

    def get_perimeter(self):
        perimeter = 2*pi*self._radius
        return perimeter

    def get_area(self):
        area = pi*self._radius*self._radius
        return area

    def compare(self):
        if self.get_perimeter() > self.get_area():
            self._color = "green"
        elif self.get_perimeter() < self.get_area():
            self._color = "blue"
        else:
            self._color = "red"
