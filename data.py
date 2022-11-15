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
        'in' : 'sewer',
        'down' : 'sewer',
        'enter' : 'sewer',
        'north' : 'north road',
        'south' : 'south road'
    },
    'sewer' : {
        'up' : 'sewer cap',
        'exit' : 'sewer cap',
        'east' : 'tunnel'
    },
    'tunnel' : {
        'west' : 'sewer',
        'east' : 'fork factory'
    },
    'fork factory' : {
        'west' : 'tunnel',
        'east' : 'factory road'
    },
    'factory road' : {
        'west' : 'fork factory',
        'east' : 'metal factory'
    },
    'metal factory' : {
        'west' : 'factory road',
        'item' : 'metal'
    }
}