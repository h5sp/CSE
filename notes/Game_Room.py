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

class Player(object):
    def __init__(self, name, health, starting_location):
        self.name = name
        self.health = health
        self.current_location  = starting_location

    def move(self, new_location):
        """This moves the player to a new room
        :param new_location: the room object of which you are ging to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """this method searches the current room to see if a room exists in that direction
        :param direction: the direction yu want to move to
        :return: the room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


OFFICE = Room("Office", " This is the office there is a answering machine in front of you")
PASILLO_CENTRAL = ("Pasillo central", "It is very dark in here! ")
PARTY_ROOM1 = ("Party room 1", " This is where the younger kids eat and party ...ITS a big MESS."
                               "There is also flash light here")
PARTY_ROOM2 = Room("Party room 2", "The door is locked!")
PARTY_ROOM4 = Room("Party room 4", "There are a couple of batteries in here.")
PARTY_ROOM3 = Room("Party room 3", "There is a couple of tables here.")
SECRET_ROOM = Room("Secret room", "The door to enter is locked! Find the key .")
Parts_and_services = Room("Parts and services", "This is where all spare equipment is at!")
Main_Hall = Room("Main hall", "This is the main hall! ")
Girls_Bathroom = Room("Girls bathroom", "This is the Girls Bathroom")
Boys_Bathroom = Room("Boys bathroom", "")
Game_Area = Room("Game area", "")
Show_Stage = Room("Show stage", "")
Dinning_Room = Room("Dinning Room", "")
Prize_Corner = Room("Prize Corner", "")
Kids_Cove = Room("Kids cove", "")
Exit = Room("Exit", "")
