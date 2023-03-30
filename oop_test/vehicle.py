from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def getBrand(self):
        pass
    
    @abstractmethod
    def timeSofiaToBurgas(self):
        pass