def showInstructions():
    print('''
RPG Game
========
Commands:
    go [direction]
    get [item]
''')

def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    if currentRoom == 'sewers':
        print('The ground to the east looks soft enough to dig if you have a shovel.')
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

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
        'west' : 'sewers'
    }
}
usedRooms = {"kitchen"}
currentRoom = 'kitchen'
showInstructions()

while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('> ')
    move = move.lower().split()

    #if they type 'teleport' first
    if move[0] == 'teleport':
        #check that they are allowed wherever they want to go
        newRoom = " ".join(move[1:])
        if newRoom in usedRooms:
            #set the current room to the new room
            currentRoom = newRoom
        #there is no door (link) to the new room
        else:
            print('You must explore that room before you can teleport there!')

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            if rooms[currentRoom][move[1]] == "tunnel" and not "shovel" in inventory:
                print("You can\'t dig without a shovel!")
            else:
                currentRoom = rooms[currentRoom][move[1]]
                usedRooms.add(currentRoom)
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break