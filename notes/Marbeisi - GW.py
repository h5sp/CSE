
class Room(object):
    def __init__(self, name, north=None, south=None, west=None, east=None, north_west=None, north_east=None,
                 west_north=None, east_north=None, south_east=None):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.north_west = north_west
        self.north_east = north_east
        self.west_north = west_north
        self.east_north = east_north
        self.south_east = south_east
        self.items = []


office = Room("Office", "The office")
Pasillo_central = Room("Pasillo_central", "This is El Pasillo Central")
Party_Room1 = Room("Party_Room1", "This is the party room 1")
Party_Room2 = Room("Party_Room2", "This is Party room 2")
Party_Room3 = Room("Party_Room3", "This is Party room 3")
Party_Room4 = Room("Party_Room4", "This is Party room 4")
Secret_Room = Room("Secret_Room", "This is the Secret room")
Parts_and_Services = Room("Parts_amd Services", "This is the Parts and services Room")
Main_hall = Room(" Main_hall", "This is the main hall")
Girls_Bathroom = Room("Girls_Bathroom", "This is the girls bathroom")
Boys_Bathroom = Room("Boys_Bathroom", "This is the boys bathroom")
Game_Area = Room("Game_Area", "This is the game area!")
Show_stage = Room("Show_stage", "This is the show stage!")
Dining_Room = Room("Dining_Room", "This is the Dining Room!")
Prize_Corner = Room("Prize_Corner", "This is the prize corner!")
Kids_Cove = Room("Kids_Cove", "This is the kids cove1")
Exit = Room("Exit", "Sorry there is no Exit!")

office.north = Pasillo_central
Pasillo_central.west = Party_Room1
Pasillo_central.east = Party_Room2
Pasillo_central.north_west = Party_Room3
Pasillo_central.north_east = Party_Room4
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
