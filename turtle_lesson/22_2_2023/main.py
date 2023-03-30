from turtle import *

from triangle import Triangle
from reactangle import Reactangle
from comparator import Comparator
from circle import Circle

if __name__ == "__main__":
    triangle = Triangle(pen, 100, 100, 140)
    triangle.compare()
    triangle.Draw()
    
    reactangle = Reactangle(pen, 30, 100)
    reactangle.compare()
    reactangle.Draw()
    
    compatator = Comparator(pen, 150, 100)
    compatator.compare()
    compatator.Draw()
    
    circle = Circle(pen, 50)
    circle.compare()
    circle.Draw()
    done()