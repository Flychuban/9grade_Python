from entity import Entity

class Orc(Entity):
    def __init__(self, name, maxhealth, berserk_index):
        super().__init__(name, maxhealth)
        self._berserk_index = berserk_index
    
    def beat_damage(self, receiver: Entity):
        if self._berserk_index < 1:
            self._berserk_index = 1
        elif self._berserk_index > 2:
            self._berserk_index = 2
        
        sum_dmg = self.attack() * self._berserk_index
        receiver.take_damage(sum_dmg)
        