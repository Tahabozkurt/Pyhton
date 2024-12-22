import random
from item import Item

# Weapon sınıfı: Saldırı için kullanılan eşyaları temsilen Item'dan türetilmiş bir sınıf
class Weapon(Item):
    def __init__(self, name, weight, damage):
        super().__init__(name, weight)
        self.damage = damage  # Silahın saldırı gücü

    def get_attack_power(self):
        # Şans faktörü ile saldırı gücünü hesapla
        luck_factor = random.uniform(0.5, 1.5)
        return self.damage * luck_factor

    def use(self):
        return self.get_attack_power()

    @staticmethod
    def miss_attack():
        # %20 ihtimalle saldırıyı kaçır
        if random.random() < 0.2:
            return True  # Saldırı kaçırıldı
        return False  # Saldırı başarılı
