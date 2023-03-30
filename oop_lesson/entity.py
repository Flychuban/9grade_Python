from weapon import Weapon

class Entity:
    def __init__(self, name, maxhealth):
        self._name = name
        self._maxhealth = maxhealth
        self._health = self._maxhealth
        self._weapon = 0

    def has_weapon(self):
        return True if self._weapon else False
    
    def equip_weapon(self, new_weapon: Weapon):
        self._weapon = new_weapon
    
    def get_health(self):
        return int(self._health)

    def is_alive(self):
        return True if self._health > 0 else False
    
    def attack(self):
        return self._weapon.GetDamage()

    def take_damage(self, damage_pts):
        if self._health > 0:
            self._health -= damage_pts
        if self._health < 0:
            self._health = 0

    def take_healing(self, healing_pts):
        if self.is_alive() is False:
            return False
        else:
            self._health += healing_pts
            if self._health > self._maxhealth:
                self._health = self._maxhealth
            return True
