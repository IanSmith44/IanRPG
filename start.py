from data import usedRooms, inventory, rooms
def showInstructions():
    print('')
    print('')
    print('')
    print('')
    print('''A fork factory has been shut down and you are the only one who can save it. You must find the metal to start the factory and then get the forks to the store.
You can use the map to see where you are and where you can go.
''')
    print('''
Battle For the forks
========
Commands:
    go [direction]
    teleport [room]
    get [item]
    use [item]
    map (shows map)
''')