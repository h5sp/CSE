class Item(object):
        def __init__(self, name):
            self.name = name


class Weapon(Item):
        def __init__(self, name, damage):
            super(Weapon, self).__init__(name)
            self.name = name
            self.damage = damage


baseballbat = Weapon("Base ball bat", 15)
pitchfork = Weapon("Pitchfork", 20)
axe = Weapon("Axe", 10)


class Armor(Item):
    def __init__(self, name, armor):
        super(Armor, self).__init__(name)
        self.armor = armor


class Character(object):
    def __init__(self, name):
        self.name = name


class Player(Character):
    def __init__(self, name, description):
        super(Character, self).__init__(name)
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
    def __init__(self, name, inflict_damage):
        super(Enemies, self).__init__(name)
        self.name = name
        self.health = 100
        self.inventory = []
        self.inflict_damage = inflict_damage

    def attack(self):
        print("enemy slaps you.")
        Player.health -= self.inflict_damage


mike = Enemies("mike", 10)
mike.attack()

