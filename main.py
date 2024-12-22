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

from character import Character
from dark_knight import DarkKnight
from health_potion import HealthPotion  # HealthPotion'u doğru dosyadan import ediyoruz
from weapon import Weapon  # Silahları import ediyoruz
import random  # Şans faktörü için random modülünü ekledik

def try_drink_health_pot(character):
    if random.random() < 0.2:  # %20 ihtimalle can potu kullanımı
        health_potion = HealthPotion()
        heal_amount = health_potion.use()  # HealthPotion'un use() fonksiyonunu çağırıyoruz
        character.health += heal_amount
        character.health = min(character.health, 250)  # Sağlık puanının maksimum değeri aşmaması için sınırla
        print(f"{character.name} used a health potion and restored {heal_amount:.2f} health. Current health: {character.health:.2f}")

if __name__ == "__main__":
    # Kullanıcıdan karakter seçimi alalım
    print("Karakter seçin:")
    print("1. Piyade")
    print("2. Süvari")
    print("3. Okçu")
    print("4. Büyücü")
    choice = int(input("Seçiminiz (1-4): "))

    if choice == 1:
        hero = Character("Piyade", health=250)
    elif choice == 2:
        hero = Character("Süvari", health=250)
    elif choice == 3:
        hero = Character("Okçu", health=250)
    elif choice == 4:
        hero = Character("Büyücü", health=250)
    else:
        print("Geçersiz seçim! Varsayılan olarak Piyade seçildi.")
        hero = Character("Piyade", health=250)

    # Karaktere başlangıçta bir silah ve sağlık potu ekleyelim
    starting_weapon = Weapon("Varsayılan Kılıç", weight=5, damage=25)
    health_potion = HealthPotion()
    hero.add_item(starting_weapon)
    hero.add_item(health_potion)

    # Düşman olarak Kara Şövalye seçelim
    villain = DarkKnight()

    # Round sistemi ile savaşı başlatalım
    round_number = 1
    while hero.is_alive() and villain.is_alive():
        input(f"Press Enter to start round {round_number}...")
        print(f"--- Round {round_number} ---")

        # Hero saldırıyor
        if Weapon.miss_attack():
            print(f"{hero.name} missed the attack!")
        else:
            damage = hero.attack()
            villain.take_damage(damage)
            villain.health = max(villain.health, 0)
            print(f"{hero.name} attacks with {damage:.2f} damage. {villain.name} health: {villain.health:.2f}")

        # Eğer villain yenildiyse
        if not villain.is_alive():
            print(f"{villain.name} is defeated!")
            break

        # Villain saldırıyor
        if Weapon.miss_attack():
            print(f"{villain.name} missed the attack!")
        else:
            damage = villain.attack()
            hero.take_damage(damage)
            hero.health = max(hero.health, 0)
            print(f"{villain.name} attacks with {damage:.2f} damage. {hero.name} health: {hero.health:.2f}")

        # Eğer hero yenildiyse
        if not hero.is_alive():
            print(f"{hero.name} is defeated!")
            break

        # Sağlık potu kullanımı kontrolü
        try_drink_health_pot(hero)
        try_drink_health_pot(villain)

        round_number += 1

    print("Savaş sona erdi!")
