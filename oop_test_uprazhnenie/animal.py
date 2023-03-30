from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, sound):
        self.__name = name
        self.__sound = sound
     
    @abstractmethod
    def getSound(self):
        return self.__sound
    
    @abstractmethod
    def getName(self):
        return self.__name
       

