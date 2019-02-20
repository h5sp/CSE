class Room(object):
    def __init__(self, name, north=None, south=None, west=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east


office = Room("The office")
Pasillo_central = Room("This is El Pasillo Central")
Party_Room = Room("This is the party room")
Party_Room2 = Room("This is Party room 2")
Party_Room3 = Room("This is Party room 3")
Party_Room4 = Room("This is Party room 4")
Secret_Room = Room("This is the Secret room")
Parts_and_Services = Room("This is the Parts and services Room")
Main_hall = Room("This is the main hall")
Girls_Bathroom = Room("This is the girls bathroom")
Boys_Bathroom = Room("This is the boys bathroom")
Game_Area = Room("This is the game area!")
Show_stage = Room("This is the show stage!")
Prize_Corner = Room("This is the prize corner!")

