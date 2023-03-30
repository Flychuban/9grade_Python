from hero import Hero
from entity import Entity

class Healer(Hero):
    def __init__(self, name, maxhealth, nickname, healer_healing):
        super().__init__(name, maxhealth, nickname)
        self._healer_healing = healer_healing
        self
    
    def beat_healing(self, receiver: Entity):
        sum_heal = self._healer_healing
        receiver.take_healing(sum_heal)
        
    def beat_damage(self, receiver: Entity):
        sum_dmg = self.attack()
        receiver.take_damage(sum_dmg)
        