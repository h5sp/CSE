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

    }
}
