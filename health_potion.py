from item import Item
import random

# HealthPotion sınıfı: Karakterlerin sağlıklarını artırmak için kullanacakları can potu
class HealthPotion(Item):
    def __init__(self, name="Health Potion", weight=1, heal_amount=20):
        super().__init__(name, weight)
        self.heal_amount = heal_amount  # Can potunun iyileştirme miktarı

    def use(self):
        luck_factor = random.uniform(0.8, 1.2)  # Şans faktörü ile iyileştirme miktarını değiştir
        return self.heal_amount * luck_factor
