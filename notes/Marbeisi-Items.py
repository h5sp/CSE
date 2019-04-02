class Player(object):
    def __init__(self, name, description):
                    self.name = name
                    self.description = description
                    self.inventory = []
                    self.health = 100
                    self.armor = 100
                    self.weapon = weapon
                    self.take_damage = damage

    def take_damage(self, damage):
        if self.armor.armor_amt > damage:
            print("NO damage is done!")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s attacks %s for %d damage " % self.name % self.health)

    def attack(self, target):
        print("%s attacks %s for %d damage" % self.name % target.name % self.weapon.damage)


class Items(object):

    def __init__(self):
        self.name = name
        self.health = 100
        self.armor = 100
        self.inventory = 10
        self.energy = 100
        self.health_kit_inventory = 50


class Weapons(Items):
    def __init__(self, damage):
        super(Weapons, self).__init__(name)
        self.damage = damage


class Baseballbat(Items):
    def __init__(self, damage):
        super(Baseballbat, self).__init__(name, damage)
        self.damage -= 15


class Pitchfork(Weapons):
    def __init__(self):
        super(Pitchfork, self).__init__(name)
        self.damage -= 20


class Hammer(Weapons):
    def __init__(self):
        super(Hammer, self).__init__(name)
        self.damage -= 10


class Tools(Items):
    def __init__(self):
        super(Tools, self).__init__(name)
        self.inventory = []


class Nails(Tools):
    def __init__(self):
        super(Nails, self).__init__(name)
        self.inventory += 1


class Matches(Tools):
    def __init__(self):
        super(Matches, self).__init__(name)
        self.inventory += 3


class Key(Tools):
    def __init__(self):
        super(Key, self).__init__(name)
        self.inventory += 1


class Food(Items):
    def __init__(self):
        super(Food, self).__init__(name)
        self.energy = energy


class ChickenNuggets(Food):
    def __init__(self):
        super(ChickenNuggets, self).__init__(name)
        self.energy += 5


class EnergyDrinks(Food):
    def __init__(self):
        super(EnergyDrinks, self).__init__(name)
        self.energy += 10


class HealthKit(Items):
    def __init__(self):
        super(HealthKit, self).__init__(name)
        self.health_Kit_Inventory = 50


class Bandages(HealthKit):
    def __init__(self):
        super(Bandages, self).__init__(name)
        self.health_Kit_Inventory += 2


class Medicine(HealthKit):
    def __init__(self):
        super(Medicine, self).__init__(name)
        self.health_Kit_Inventory += 5


class Anesthetic(HealthKit):
    def __inti__(self):
        super(Health_Kit, self).__inti__(name)
        self.health_Kit_Inventory += 5
        self.health += 5


class Scissors(HealthKit):
    def __init__(self):
        super(Scissors, self).__init__(name)
        self.health_Kit_Inventory += 2


class Electronics(Items):
    def __init__(self):
        super(Electronics, self).__init__(name)
        self.on = True
        self.off = False


class Microwave(Electronics):
    def __init__(self):
        super(Microwave, self).__init__(name)
        self.on = True
        print("The microwave is on!")
        self.off = False
        print("The microwave is off!")


class Flashlight(Electronics):
    def __init__(self):
        super(Flashlight, self).__init__(name)
        self.on = True
        print("The flashlight is on!")
        self.off = False
        print("The flashlight is off!")


class Armor(Items):
    def __init__(self):
        super(Armor, self).__init__(name)
        self.protection = protection


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__(name)
        self.protection = protection
        self.damage -= 5


class Chestplate(Armor):
    def __init__(self):
        super(Chestplate, self).__init__(name)
        self.protection = protection
        self.damage -= 5


class Shield(Armor):
    def __init__(self):
        super(Shield, self).__init__(name)
        self.protection = protection
        self.damage -= 5


Me = Player("Me", "It's me")
Me.inventory = [Shield, Scissors, Chestplate]
Me.attack()