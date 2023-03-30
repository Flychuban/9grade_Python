import random

class Weapon:
    def __init__(self, type, damage, critical_strike_percent) -> None:
        self._type = type
        self._normal_shot = damage
        self._critical_strike_percent = critical_strike_percent
        self._next_critical_hit = False
    
    def critical_hit(self):
        random_chance = random.uniform(0, 1)
        result = True if self._critical_strike_percent > random_chance else False
        if result:
            self._next_critical_hit = True
        return result
    
    
    def GetDamage(self):
        self.critical_hit()
        if self._next_critical_hit:
            return self._normal_shot * 2
        return self._normal_shot
    
    def GetType(self):
        return self._type
    def GetCriticalStrikePercent(self):
        return self._critical_strike_percent