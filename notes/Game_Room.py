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


Office = Room("Office", " This is the office there is a answering machine in front of you")
Pasillo_Central = ("Pasillo central", "It is very dark in here! ")
Party_Room1 = ("Party room 1", " This is where the younger kids eat and party ...ITS a big MESS."
                               "There is also flash light here")
Party_Room2 = Room("Party room 2", "The door is locked!")
Party_Room4 = Room("Party room 4", "There are a couple of batteries in here.")
Party_Room3 = Room("Party room 3", "There is a couple of tables here.")
Secret_Room = Room("Secret room", "The door to enter is locked! Find the key .")
Parts_and_services = Room("Parts and services", "This is where all spare equipment is at!")
Main_Hall = Room("Main hall", "This is the main hall! ")
Girls_Bathroom = Room("Girls bathroom", "This is the Girls Bathroom")
Boys_Bathroom = Room("Boys bathroom", "This is the boys bathroom")
Game_Area = Room("Game area", "This is the Game Area")
Show_Stage = Room("Show stage", "This is the Show Stage where all the fun is at!!")
Dinning_Room = Room("Dinning Room", "This is the dinning Room.")
Prize_Corner = Room("Prize Corner", "This is the prize conner where you pick up your prize!")
Kids_Cove = Room("Kids cove", "This is Kids cove where you can play at anytime!")
Exit = Room("Exit", "I'M SORRY THERE IS NO EXIT!!")


Office.north = Pasillo_Central
Pasillo_Central.west = Party_Room1
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

playing = True
current_node = world_map['OFFICE']
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'south east', 'north west', 'north  east', 'south west',
              'east north', 'east south']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I cant go that way")
    else:
        print("Command Not Found")
