usedRooms = {"kitchen"}

inventory = []

rooms = {
    'kitchen' : { 
        'east' : 'living room'
    },
    'living room' : {
        'west' : 'kitchen',
        'north' : 'garage',
        'east' : 'front door',
        'south' : 'stairs'
    },
    'garage' : {
        'south' : 'living room',
        'item' : 'shovel'
    },
    'stairs' : {
        'north' : 'living room'
    },
    'front door' : {
        'west' : 'living room',
        'east' : 'front yard'
    },
    'front yard' : {
        'west'  : 'front door',
        'east' : 'north road'
    },
    'north road' : {
        'west' : 'front yard',
        'south' : 'sewer cap'
    },
    'sewer cap' : {
        'down' : 'sewers',
        'enter' : 'sewers',
        'north' : 'north road',
        'south' : 'south road'
    },
    'sewers' : {
        'up' : 'sewer cap',
        'exit' : 'sewer cap',
        'east' : 'tunnel'
    },
    'tunnel' : {
        'west' : 'sewers',
        'east' : 'fork factory'
    },
    'fork factory' : {
        'west' : 'tunnel',
        'east' : 'road'
    }
}