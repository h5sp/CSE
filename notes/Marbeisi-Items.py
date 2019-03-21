class Items(object):
    def __init__(self):
        self.name = name
        self.health = 100
        self.armor = 100
        self.inventory = 10
        self.energy = 100
        self.health_kit_inventory = 50


class weapons(Items):
    def __init__(self, name):
        super(weapons, self).__init__(name)


class Weapons(Items):
    def __init__(self, damage):
        super(Weapons, self).__init__(name)
        self.damage = damage


class Baseballbat(Items):
    def __init__(self):
        super(Weapons, self).__init__(name)
        self.damage -= 15


class Pitchfork(weapons):
    def __init__(self):
        super(weapons, self).__init__(name)
        self.damage -= 20


class Hammer(weapons):
    def __init__(self):
        super(weapons, self).__init__(name)
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
        self.health_Kit_Inventory = 50


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
        super(health_Kit, self).__inti__(name)
        self.health_Kit_Inventory += 5
        self.health += 5


class Scissors(health_Kit):
    def __init__(self):
        super(health, self).__init__(name)
        self.health_Kit_Inventory += 2


class Electronics(electronics, on=True, off=False):
    def __init__(self):
        super(Electronics, self).__init__(name)
        self.on = True
        self.off = False


class Microwave(electronics):
    def __init__(self):
        super(electronics, self).__init__(name)
        self.on = True
        print("The microwave is on!")
        self.off = False
        print("The microwave is off!")


class Flashlight(electronics):
    def __init__(self):
        super(electronics, self).__init__(name)
        self.on = True
        print("The flashlight is on!")
        self.off = False
        print("The flashlight is off!")


class Armor(armor, protection):
    def __init__(self):
        super(Armor, self).__init__(name)
        self.protection = protection


class Helmet(armor, protection):
    def __init__(self):
        super(armor, self).__init__(name)
        self.protection = protection
        self.damage -= 5


class Chestplate(armor, protection):
    def __init__(self):
        super(armor, self).__init__(name)
        self.protection = protection
        self.damage -= 5


class Shield(armor, protection):
    def __init__(self):
        super(armor, self).__init__(name)
        self.protection = protection
        self.damage -= 5
