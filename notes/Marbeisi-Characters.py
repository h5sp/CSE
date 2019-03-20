class Item(object):
        def __init__(self, name):
            self.name = name


class Weapon(Item):
        def __init__(self, name, damage):
            super(Weapon, self).__init__(name)
            self.damage = damage


class Armor(Item):
    def __init__(self, name, armor):
        super(Armor, self).__init__(name)
        self.armor = armor


class Player(object):
    def __init__(self, name, description):
                    self.name = name
                    self.description = description
                    self.inventory = inventory
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


baseballbat = Weapon("baseballbat", 15)
pitchfork = Weapon("pitchfork", 20)
hammer = Weapon("hammer", 10)
police_armor = Armor("Police armor", 100)

orc = Character("Orcl", 100, sword, Armor("Generic Armor", 2))
orc2 = Character("Wiebe", 100, canoe, wiebe_armor)

orc.attack(orc2)
orc2.attack(orc)
orc2.attack(orc)
orc2.attack(orc)