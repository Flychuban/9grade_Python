from turtle import Turtle
from abc import ABC, abstractmethod

class Shape:
    def __init__(self, pen: Turtle) -> None:
        self._pen = pen
    
    
    @abstractmethod
    def Draw(self):
        pass