class Player(objects):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.health = 100
        self.armor = 100
        self.weapon = weapon

    def take_damage(self, damage):
        if self.armor > damage:
            print("No damage is done.")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)
