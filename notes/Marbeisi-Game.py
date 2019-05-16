import random


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = []
        self.characters = []


Office = Room("Office", " This is the office there is a answering machine in front of you")
Pasillo_Central = Room("Pasillo Central", "It is very dark in here! ")
Party_Room_1 = Room("Party Room 1", " This is where the younger kids eat and party ...ITS a big MESS.")
Party_Room2 = Room("Party Room 2", "The door is locked!")
Party_Room3 = Room("Party Room 3", "There are a couple of batteries in here.")
Party_Room4 = Room("Party Room 4", "There is a couple of tables here.")
Secret_Room = Room("Secret Room", "The door to enter is locked! Find the key .")
Parts_and_Services = Room("Parts and Services", "This is where all spare equipment is at!")
Main_hall = Room("Main hall", "This is the main hall! ")
Girls_Bathroom = Room("Girls Bathroom", "This is the Girls Bathroom")
Boys_Bathroom = Room("Boys Bathroom", "This is the boys bathroom")
Game_Area = Room("Game Area", "This is the Game Area")
Show_stage = Room("Show stage", "This is the Show Stage where all the fun is at!!")
Dining_Room = Room("Dining Room", "This is the dinning Room.")
Prize_Corner = Room("Prize Corner", "This is the prize conner where you pick up your prize!")
Kids_Cove = Room("Kids Cove", "This is Kids cove where you can play at anytime!")
Exit = Room("Exit", "I'M SORRY THERE IS NO EXIT!!")


Office.north = Pasillo_Central
Pasillo_Central.west = Party_Room_1
Pasillo_Central.east = Party_Room2
Pasillo_Central.north_west = Party_Room3
Pasillo_Central.north_east = Party_Room4
Party_Room3.west_north = Secret_Room
Secret_Room.north_east = Parts_and_Services
Parts_and_Services.east = Main_hall
Main_hall.north = Girls_Bathroom
Main_hall.north_east = Boys_Bathroom
Boys_Bathroom.south = Main_hall
Main_hall.east = Game_Area
Game_Area.east_north = Show_stage
Show_stage.south = Dining_Room
Dining_Room.south_east = Prize_Corner
Prize_Corner.south = Kids_Cove
Kids_Cove.north = Prize_Corner
Prize_Corner.north_east = Exit


class Player(object):
    def __init__(self, name, health, starting_location):
        self.name = name
        self.health = health
        self.current_location = starting_location

    def move(self, new_location):
        """This moves the player to a new room
        :param new_location: the room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """this method searches the current room to see if a room exists in that direction
        :param direction: the direction yu want to move to
        :return: the room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


ME = Player("me", 100, Office)


class Enemies(object):
    def __init__(self, name, health, inflict_damage):
        self.name = name
        self.health = health
        self.inventory = []
        self.inflict_damage = inflict_damage

    def attack(self):
        print("health:", ME.health)
        print("enemy slaps you.")
        ME.health -= self.inflict_damage
        print("mike takes 10 health points")
        print("your current health level was 100. now it's:")
        print(ME.health)


mike = Enemies("mike", 50, 10)
mike.attack()


class Items(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.armor = 100
        self.inventory = 10
        self.energy = 100
        self.health_kit_inventory = 50


class Weapons(Items):
    def __init__(self, name, health, damage):
        super(Weapons, self).__init__(name, health)
        self.damage = damage
        self.inventory = []
        if health <= damage:
            print("There is damage done!")


class Baseballbat(Weapons):
    def __init__(self, damage, inventory):
        super(Baseballbat, self).__init__(self, damage, inventory)
        self.damage -= 15
        self.inventory += 5
        print("You have swinged the bat!")
        answer = input("Do you want to pick this up?")
        print("You have answer %s , you have picked this item up!" % answer)
        if answer.lower() in ['no']:
            print("item is not picked up!")


class Pitchfork(Weapons):
    def __init__(self, damage, inventory):
        super(Pitchfork, self).__init__(self, damage, inventory)
        self.damage -= 20
        self.inventory += 10
        print("you hav picked up the pitchfork!")
        answer = input("Do you want to pick this up?")
        print("You have answer %s , you have picked this item up!" % answer)
        if answer.lower() in ['no']:
            print("item is not picked up!")


class Hammer(Weapons):
    def __init__(self, damage, inventory):
        super(Hammer, self).__init__(self, damage, inventory)
        self.damage -= 10
        self.inventory += 4
        print("you have used the hammer!")
        answer = input("Do you want to pick this up?")
        print("You have answer %s , you have picked this item up!" % answer)
        if answer.lower() in ['no']:
            print("item is not picked up!")


class Sword(Weapons):
    def __init__(self, damage, inventory):
        super(Sword, self).__init__(self, damage, inventory)
        self.damage -= 20
        self.inventory += 7
        print("You have used your sword")
        answer = input("Do you want to pick this up?")
        print("You have answer %s , you have picked this item up!" % answer)
        if answer.lower() in ['no']:
            print("item is not picked up!")


class Axe(Weapons):
    def __init__(self, damage, inventory):
        super(Axe, self).__init__(self, damage, inventory)
        self.damage -= 15
        self.inventory += 10
        answer = input("Do you want to pick this up?")
        print("You have answer %s , you have picked this item up!" % answer)
        if answer.lower() in ['no']:
            print("item is not picked up!")


class Tools(Items):
    def __init__(self, inventory, name, health):
        super(Tools, self).__init__(name, health)
        self.inventory = inventory

    def nails(self):
        self.inventory += 1
        print("This has been added to your inventory!")

    def matches(self):
        self.inventory += 3
        print("This has been added to your inventory!")

    def key(self):
        self.inventory += 1
        print("This has been added to your inventory!")


class Energy(object):
    def __init__(self, energy, name):
        super(Energy, self).__init__(name)
        self.energy = energy

    def food(self, energy):
        self.energy = energy

    def chickennuggets(self):
        self.energy += 5
        print("Your energy has been boosted up!")

    def energydrinks(self):
        self.energy += 10
        print("Your energy has been boosted up!")


class HealthKit(object):
    def __init__(self, name, health):
        super(HealthKit, self).__init__(name, health)
        self.health_Kit_Inventory = 50
        self.health = health

    def bandages(self):
        self.health_Kit_Inventory += 2
        print("Your health kit has more stuff now!")
        print("You can use any of this anytime!")

    def medicine(self):
        self.health_Kit_Inventory += 5
        print("Your health kit has more stuff now!")
        print("You can use any of this anytime!")

    def anesthetic(self):
        self.health_Kit_Inventory += 5
        self.health += 5
        print("Your health kit has more stuff now!")
        print("You can use any of this anytime!")

    def scissors(self):
        self.health_Kit_Inventory += 2
        print("Your health kit has more stuff now!")
        print("You can use any of this anytime!")


class Electronics(object):
    def __init__(self, on):
        self.on = on

    def microwave(self):
        print("The flashlight is on!")
        self.on = True
        answer = input("turn off?>_")
        if answer.lower() in ['yes']:
            print("The flashlight is off!")
            self.on = False

    def flashlight(self):
        print("The flashlight is on!")
        self.on = True
        answer = input("turn off?>_")
        if answer.lower() in ['yes']:
            print("The flashlight is off!")
            self.on = False


class Armor(object):
    def __init__(self, protection, damage):
        self.protection = protection
        self.damage = damage


class Helmet(Armor):
    def __init__(self, damage, health):
        super(Helmet, self).__init__(damage, health)
        self.damage = damage
        self.health = health
        self.damage -= 5
        self.health -= 5
        print("Some damage was done.")


class Chestplate(Armor):
    def __init__(self, protection, damage, health):
        super(Chestplate, self).__init__(damage, health)
        self.protection = protection
        self.damage = damage
        self.health = health
        self.damage -= 5
        self.health -= 5
        print("Some damage was done.")


class Shield(Armor):
    def __init__(self, damage, health, protection):
        super(Shield, self).__init__(damage, health)
        self.damage = damage
        self.protection = protection
        self.health = health
        self.damage -= 5
        self.health -= 5
        print("Some damage was done.")

    @staticmethod
    def defend():
        damage_took = mike.inflict_damage
        if Enemies.attack:
            print("You took damage:", damage_took)
            if damage_took == 0:
                print("no damage was done.")
            elif damage_took >= 1:
                print("damage was done.")
                ME.health -= damage_took


playing = True

directions = ['north', 'south', 'west', 'east', 'up', 'down', 'south east', 'north west', 'north  east', 'south west',
              'east north', 'east south']

while playing:
    print("-", ME.current_location.name)
    print("-", ME.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit', 'ee']:
        playing = False
        if command.lower() in directions:
            try:
                room_name = getattr(ME.current_location, command.lower())
                ME.move(room_name)
            except KeyError:
                print("Error: Can't go that way")
        else:
            print("cant go that way")
