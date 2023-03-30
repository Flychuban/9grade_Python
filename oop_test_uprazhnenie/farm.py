from animal import Animal

class Farm():
    def __init__(self, farm_name):
        self.__farm_name = farm_name
        self.__animals = []
    
    def getName(self):
        return self.__farm_name
    
    def makeSounds(self):
        for animal in self.__animals:
            print(animal.getSound())
    
    def addAnimal(self, animal: Animal):
        self.__animals.append(animal)
            
    def makeSound(self, number_animal):
        print(self.__animals[number_animal].getSound())
