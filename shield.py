from item import Item
import random

# Shield sınıfı: Savunma için kullanılan eşyaları temsilen Item'dan türetilmiş bir sınıf
class Shield(Item):
    def __init__(self, name, weight, defense_value, durability):
        super().__init__(name, weight)
        self.defense_value = defense_value  # Kalkanın savunma gücü
        self.durability = durability  # Kalkanın dayanıklılığı

    def use(self):
        if self.durability > 0:
            luck_factor = random.uniform(0.5, 1.5)  # Şans faktörü
            self.durability -= 1
            return self.defense_value * luck_factor
        else:
            return 0  # Kalkan dayanıklılığı bittiğinde savunma gücü sağlamaz
