from horse import Horse
from cat import Cat
from dog import Dog
from sheep import Sheep
from pig import Pig 

from farm import Farm
from animal import Animal

horse = Horse("Horse", "Neigh")
cat = Cat("Cat", "Meow")
dog = Dog("Dog", "Woof")
sheep = Sheep("Sheep", "Baa")
pig = Pig("Pig", "Oink")

animals = [horse, cat, dog, sheep, pig]

farm = Farm("Pesho Farm")

for animal in animals:
    farm.addAnimal(animal)

farm.makeSounds()
farm.makeSound(2)


print(f"Far name: {farm.getName()}")