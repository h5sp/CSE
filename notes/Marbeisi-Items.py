class Items(objects):
    def __init__(self, name):
        self.name = name
        sef.health = 100


class Weapon(weapons):
    def __init__(self, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Food(food):
    def __init__(self, energy):
        super(Food, self).__init__(name)
        self.energy = energy


class HealthKit(healthkit, health):
    def __init__(self):
        super(Healht_kit, self).__init__(name)
        self.health = health


class Electronics(electronics, usefull):
    def __init__(self):
        super(Electronics, self).__init__(name)
        self.useful = useful


class Armor(armor, protection):
    def __init__(self):
        super(Armor, self).__init__(name)
        self.protection = protection
