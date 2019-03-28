world_map = {
    'OFFICE': {
        'NAME': "The office",
        'DESCRIPTION': " This is the office there is a answering machine in front of you ",
        'PATHS': {
            'NORTH': "Pasillo Central",
        }
    },
    'PASILLO CENTRAL': {
        'NAME': " The Pasillo Central",
        'DESCRIPTION': "It is very dark in here! ",
        'PATHS': {
            'WEST': "Party room 1",
            'EAST': "Party room 2"
        }
    },
    'PARTY ROOM 1': {
        'NAME': "Party room 1 ",
        'DESCRIPTION': "There is a flash light here ",
        'PATHS': {
            'SOUTH': "PARTY ROOM 2"

        }
    },
    'PARTY ROOM 2 ': {
        'NAME': "The party room 2",
        'DESCRIPTION': "The door is locked!",
        'PATHS': {
            'NORTH EAST': "Party room 4",
            'NORTH WEST': "Party room 3"

        }
    },
    'PARTY ROOM 4': {
        'NAME': "The party room 4",
        'DESCRIPTION': "There are a couple of batteries in here.",
        'PATHS': {
            'WEST': "Pasillo Central"

        }

    },
    'Party ROOM 3': {
        'NAME': "The party room 3",
        'DESCRIPTION': "There is a couple of tables here.",
        'PATHS': {
            'NORTH': "Secret room",

        }
    },
    'SECRET ROOM': {
        'NAME': "Secret room",
        'DESCRIPTION': "The door to enter is locked! Find the key .",
        'PATHS': {
            'SOUTH': "Party room 3"

        }
    },
    'Parts and services': {
        'Name': "Parts and services",
        'DESCRIPTION': "This is where all spare equipment is at!",
        'PATHS': {
            'EAST': "Main Hall"
        }
    },
    'Main Hall': {
        'NAME': "Main Hall",
        'DESCRIPTION': "This is the main hall! ",
        'PATHS': {
            'NORTH': "Girls Bathroom",
            'NORTH EAST': "Boys Bathroom"
        }
    },
    'Girls Bathroom': {
        'NAME': "Girls Bathroom",
        'DESCRIPTION': "This is the Girls Bathroom",
        'PATHS': {
            'SOUTH': "Main Hall"
        }
    },
    'Boys Bathroom': {
        'NAME': "Girls Bathroom",
        'DESCRIPTION': "This is the boys bathroom",
        'PATHS': {
            'SOUTH': "Main Hall",
            'SOUTH EAST': "Game Area"
        }
    },
    'Game Area': {
        'NAME': "Game Area",
        'DESCRIPTION': "This is the Game Area",
        'PATHS': {
            'EAST NORTH': "Show Stage",
            'EAST SOUTH': "Dinning Room"
        }
    },
    'Show Stage': {
        'NAME': "Show Stage",
        'DESCRIPTION': "This is the Show Stage where all the fun is at!!",
        'PATHS': {
            'SOUTH WEST': "Game Area",
            'SOUTH': "Dinning Room"
        }
    },
    'Dinning Room': {
        'NAME': "Dinning Room",
        'DESCRIPTION': "This is the dinning Room.",
        'PATHS': {
            'SOUTH EAST': "Prize Corner",
            'EAST': "Exit"
        }
    },
    'Prize Corner': {
        'NAME': "Prize Corner",
        'DESCRIPTION': "This is the prize conner where you pick up your prize!",
        'PATHS': {
            'SOUTH': "Kids Cove",
            'NORTH WEST': "Dinning Room",
            'NORTH EAST': "EXIT"
        }
    },
    'Kids Cove': {
        'NAME': "Kids Cove",
        'DESCRIPTION': "This is Kids cove where you can play at anytime!",
        'PATHS': {
            'NORTH': "Prize Corner",
        }
    },
    'EXIT': {
        'NAME': "EXIT",
        'DESCRIPTION': "I'M SORRY THERE IS NO EXIT!!"

    },

}
playing = True
current_node = world_map['OFFICE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN', 'SOUTH EAST', 'NORTH WEST', 'NORTH EAST', 'SOUTH WEST',
              'EAST NORTH', 'EAST SOUTH']

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

