from data import usedRooms, inventory, rooms
def showStatus(currentRoom):
    print('---------------------------')
    print('You are in the ' + currentRoom)
    if currentRoom == 'sewers':
        print('The ground to the east looks soft enough to dig if you have a shovel.')
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
