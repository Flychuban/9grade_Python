from turtle import Turtle
from shape import Shape
import turtle

class Triangle(Shape):
    def __init__(self, pen: Turtle, first_line, second_line, third_line) -> None:
        super().__init__(pen)
        self._first_line = first_line
        self._second_line = second_line
        self._third_line = third_line
        self._color = "white" 
        
    def Draw(self):
        turtle.penup()
        turtle.goto(200, 200)
        turtle.pendown()
        turtle.fillcolor(self._color)
        turtle.begin_fill()
        turtle.forward(self._first_line)
        turtle.left(90)
        turtle.forward(self._second_line)
        turtle.left(135)
        turtle.forward(self._third_line)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(230, 220)
        turtle.pendown()
        label = "Perimeter: " if self._color == "green" else "Area: "
        func = self.get_perimeter() if self._color == "green" else self.get_area()
        turtle.write(f"{label}{func}", font=("Arial", 10, "normal"))
    
    def get_perimeter(self):
        perimeter = self._first_line + self._second_line + self._third_line
        return perimeter
    
    def get_area(self):
        # width = abs(self._first_pt[0] - self._second_pt[0])
        # height = abs(self._second_pt[1])
        # area = (width*height)/2
        # print(f"S: {area}")
        
        #find the minimal line in triangle
        max_line = max(self._first_line, self._second_line, self._third_line)
        shorter_lines = [line for line in [self._first_line, self._second_line, self._third_line] if line != max_line]
        area = shorter_lines[0] * shorter_lines[1] / 2
        return area
    
    def compare(self):
        if self.get_perimeter() > self.get_area():
            self._color = "green"
        elif self.get_perimeter() < self.get_area():
            self._color = "blue"
        else:
            self._color = "red"
