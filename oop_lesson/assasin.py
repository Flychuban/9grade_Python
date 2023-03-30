from hero import Hero
from entity import Entity

class Assasin(Hero):
    def __init__(self, name, maxhealth, nickname):
        super().__init__(name, maxhealth, nickname)
            
    def beat_damage(self, receiver: Entity):
        sum_dmg = self.attack()         
        receiver.take_damage(sum_dmg)