import random
from weapon import Weapon

# Karakterler arasındaki dövüş mekanizması
def fight(hero, villain):
    round_number = 1
    while hero.is_alive() and villain.is_alive():
        input(f"Press Enter to start round {round_number}...")
        print(f"--- Round {round_number} ---")

        # Hero saldırıyor
        damage = hero.attack()
        villain.take_damage(damage)
        villain.health = max(villain.health, 0)
        print(f"{hero.name} attacks with {damage:.2f} damage. {villain.name} health: {villain.health:.2f}")

        # Eğer villain yenildiyse
        if not villain.is_alive():
            print(f"{villain.name} is defeated!")
            break

        # Villain saldırıyor
        if villain.weapon is None:  # Eğer düşmanın silahı yoksa varsayılan bir silah kuşan
            villain.equip_weapon(Weapon("Kara Kılıç", weight=8, damage=35))
        damage = villain.attack()
        hero.take_damage(damage)
        hero.health = max(hero.health, 0)
        print(f"{villain.name} attacks with {damage:.2f} damage. {hero.name} health: {hero.health:.2f}")

        # Eğer hero yenildiyse
        if not hero.is_alive():
            print(f"{hero.name} is defeated!")
            break

        # Sağlık potu kullanımı kontrolü
        if random.random() < 0.2:  # %20 ihtimalle can potu kullanımı
            hero.drink_health_pot()
        if random.random() < 0.2:  # %20 ihtimalle can potu kullanımı
            villain.drink_health_pot()

        round_number += 1

    print("Savaş sona erdi!")
