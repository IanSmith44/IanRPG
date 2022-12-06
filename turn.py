from data import usedRooms, inventory, rooms
def showStatus(currentRoom):
    print('---------------------------')
    print('You are in the ' + currentRoom)
    if currentRoom == 'sewer':
        print('The ground to the east looks soft enough to dig if you have a shovel.')
    if currentRoom == 'fork factory' and 'metal' not in inventory:
        print('The Fork Factory is shut down, it looks like it ran out of metal. You should head east towards the metal factory.')
    if currentRoom == 'fork factory' and 'metal' in inventory:
        print('The Fork Factory is closed, you can use the metal to start the factory.')
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
def map():
    print('''
                     [Garage]
                        |
    [Kitchen] -- [Living Room] -- [Front Door] -- [Front Yard] -- [Northern Road]
                        |                                                |
                     [Stairs]                                       [Sewer Cap] ~~~~ [Sewers]
                                                                        |              |
                                                                      [Road]        [Tunnel]
                                                                        |              |
                                                                     [Store]     [Fork Factory]
                                                                        |              |
                                                                   [Fork Aisle]      [Road]
                                                                                       |
                                                                                 [Metal Factory]''')
