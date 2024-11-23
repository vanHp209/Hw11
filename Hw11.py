class Character:
    def __init__(self, name):
        self.name = name  # Публичное поле
        self.__health = 100  # Приватное поле для здоровья
        self.__energy = 100  # Приватное поле для энергии
        self.__weapon = None  # Приватное поле для оружия

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} атакует с использованием {self.__weapon if self.__weapon else 'рук'}!")
        else:
            print("Недостаточно энергии для атаки.")

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health > 0:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.__health}.")
        else:
            self.__health = 0
            print(f"Персонаж {self.name} погиб.")


    def get_status(self):
         weapon_status = self.__weapon if self.__weapon else "Без оружия"
         return f"Статус персонажа {self.name}:\nЗдоровье: {self.__health}\nЭнергия: {self.__energy}\nОружие: {weapon_status}"


if __name__ == "__main__":
    hero = Character("Артур")
    print(hero.get_status())

    hero.equip_weapon("Меч")
    hero.attack()
    print(hero.get_status())

    hero.take_damage(30)
    print(hero.get_status())

    hero.take_damage(80)
