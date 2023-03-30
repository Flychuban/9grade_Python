from entity import Entity

class Hero(Entity):
    def __init__(self, name, maxhealth, nickname):
        super().__init__(name, maxhealth)
        self._nickname = nickname
        
    def __repr__(self) -> str:
        return f"{self._name} {self._nickname}"
    
