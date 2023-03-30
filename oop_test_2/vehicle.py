from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def getBrand(self):
        pass

    @abstractmethod
    def timeSofiaToBurgas(self):
        pass
    
    @abstractmethod
    def getSpeed(self):
        pass