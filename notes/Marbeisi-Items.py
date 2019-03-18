class Items(objects):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 100
        self.inventory = 10
        self.energy = 100
        self.health_kit_inventory = 50


class Weapon(weapons):
    def __init__(self, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Baseballbat(weapons):
    def __init__(self):
        super(weapon, self).__init__(name)
        self.damage -= 15


class Pitchfork(weapons):
    def __init__(self):
        super(weapon, self).__init__(name)
        self.damage -= 20


class Hammer(weapons):
    def __init__(self):
        super(weapon, self).__init__(name)
        self.damage -= 10


class Tools(tools):
    def __init__(self):
        super(tools, self).__init__(name)
        self.inventory = inventory


class Hammer2(tools):
    def __init__(self):
        super(tools, self).__init__(name)
        self.inventory += 2


class Nails(tools):
    def __init__(self):
        super(tools, self).__init__(name)
        self.inventory += 1


class Matches(tools):
    def __init__(self):
        super(tools, self).__init__(name)
        self.inventory += 3


class Key(tools):
    def __init__(self):
        super(tools, self).__init__(name)
        self.inventory += 1


class Food(food):
    def __init__(self, energy):
        super(Food, self).__init__(name)
        self.energy = energy


class ChickenNuggets(food):
    def __init__(self):
        super(food, self).__init__(name)
        self.energy += 5


class EnergyDrinks(food):
    def __init__(self):
        super(food, self).__init__(name)
        self.energy += 10


class HealthKit(healthkit, health):
    def __init__(self):
        super(health_kit, self).__init__(name)
        self.health_Kit_Inventory = inventory


class Bandages(health_Kit):
    def __init__(self):
        super(health, self).__init__(name)
        self.health_Kit_Inventory += 2


class Medicine(health_Kit):
    def __init__(self):
        super(health, self).__init__(name)
        self.health_Kit_Inventory += 5


class Anesthetic(health_Kit):
    def __inti__(self):
        super(health, self).__inti__(name)
        self.health_Kit_Inventory += 5


class Scissors(health_Kit):
    def __init__(self):
        super(health, self).__init__(name)
        self.health_Kit_Inventory +

class Electronics(electronics, usefull):
    def __init__(self):
        super(Electronics, self).__init__(name)
        self.useful = useful


class Armor(armor, protection):
    def __init__(self):
        super(Armor, self).__init__(name)
        self.protection = protection
