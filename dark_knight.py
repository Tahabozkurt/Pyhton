from character import Character
from weapon import Weapon
from shield import Shield

# DarkKnight sınıfı: Özel bir düşman karakteri
class DarkKnight(Character):
    def __init__(self, name="Kara Şövalye", health=250):
        super().__init__(name, health)
        self.equip_weapon(Weapon("Kara Mızrak", weight=10, damage=28))
        self.equip_shield(Shield("Kara Kalkan", weight=15, defense_value=20, durability=5))
