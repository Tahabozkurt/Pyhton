from health_potion import HealthPotion
from weapon import Weapon
import random

# Character sınıfı: Oyundaki karakterleri modellemek için kullanılacak temel sınıf
class Character:
    def __init__(self, name, health, inventory=None):
        self.name = name  # Karakterin adı
        self.health = health  # Karakterin sağlık puanı
        self.weapon = None  # Karakterin kuşanabileceği silah
        self.shield = None  # Karakterin kuşanabileceği kalkan
        self.inventory = inventory if inventory else []  # Karakterin envanteri

    def equip_weapon(self, weapon):
        self.weapon = weapon  # Karaktere bir silah kuşandıralım

    def equip_shield(self, shield):
        self.shield = shield  # Karaktere bir kalkan kuşandıralım

    def attack(self):
        if self.weapon:
            return self.weapon.use()  # Silahın gücüne bağlı olarak saldırı yap
        else:
            # Eğer silah yoksa varsayılan bir silah kuşan
            self.equip_weapon(Weapon("Varsayılan Kılıç", weight=5, damage=30))
            return self.weapon.use()

    def take_damage(self, damage):
        self.health -= max(damage, 0)  # Hasarı sağlıktan düş (negatif olmasın)
        self.health = max(self.health, 0)  # Sağlık puanını negatif olmaması için sıfırın altına sabitle

    def is_alive(self):
        return self.health > 0  # Karakterin yaşıyor olup olmadığını kontrol et

    def drink_health_pot(self):
        # Can potu kullanarak sağlık artırımı
        if random.random() < 0.2:  # %20 ihtimalle can potu kullanımı
            health_potion = HealthPotion()
            heal_amount = health_potion.use()  # HealthPotion'un use() fonksiyonunu çağırıyoruz
            self.health += heal_amount
            self.health = min(self.health, 250)  # Sağlık puanının maksimum değeri aşmaması için sınırla
            print(f"{self.name} used a health potion. Current health: {self.health:.2f}")

    def add_item(self, item):
        # Envantere yeni bir eşya ekle
        self.inventory.append(item)
        print(f"{self.name} added {item.name} to inventory.")

    def delete_item(self, item):
        # Envanterden bir eşya çıkar
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{self.name} removed {item.name} from inventory.")
        else:
            print(f"{item.name} not found in {self.name}'s inventory.")
