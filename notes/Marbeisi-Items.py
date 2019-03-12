class Items(objects):
    def __init__(self, name):
        self.name = name
        sef.health = 100


class Weapon(weapons):
    def __init__(self):
        self.baseball_bat = baseball_bat
        self.pitchfork = pitchfork
        self.hammer = hammer
        self.nails = nails
        self.matches = matches
        self.key = key


class Food(food):
    def __init__(self):
        self.chicken_nuggets = chicken_nuggets
        self.ketchup = ketchup
        self.energy_drinks = energy_drinks


class HealthKit(healthkit):
    def __init__(self):
        self.bandages = bandages
        self.medicine = medicine
        self.anesthetic = anesthetic
        self.scissors = scissors
        self.alcohol = alcohol


class Electronics(electronics):
    def __init__(self):
        self.microwave = microwave
        self.flashlight = flashlight
        self.batteries = batteries
        self.watch = watch


class Clothes(clothes):
    def __init__(self):
        self.T_shirts = T_shirts
        self.jeans = jeans
        self.shoes = shoes
        self.socks = socks
        self.beanie = beanie
