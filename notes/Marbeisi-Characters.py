class Item(object):
        def __init__(self, name):
            self.name = name


class Weapon(Item):
        def __init__(self, name, damage):
            super(Weapon, self).__init__(name)
            self.damage = damage
            self.baseballbat = damage
            self.pitchfork = damage
            self.hammer = damage


class Armor(Item):
    def __init__(self, name, armor):
        super(Armor, self).__init__(name)
        self.armor = armor


class Player(Character):
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
            print("No damage is done!")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s attacks %s for %d damage " % self.name % self.health)

    def attack(self, target):
        print("%s attacks %s for %d damage" % self.name % target.name % self.weapon.damage)


class Enemies(Character):
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.take_damage = damage
        self.inflict_damage = inflict_damage

    @staticmethod
    def attack():
        print("You have attacked the player!")
    if baseballbat >= 15:
        return "damage"
    else pitchfork >= 20:
        return "damage"



player = Character("")
enemies = Character("")
