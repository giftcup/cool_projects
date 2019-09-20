import random

def showInstructions():
    print('''
    RPG Game
    ========
    Commands:
        Welcome! To win, traverse 3 rooms and collect the elements without the monster eating you.BON CHANCE
        go [direction]
        get [element]

 ''')

def showstatus():
    #print player's current status
    print('-------------------')
    print('You are in the '+ currentRoom)
    #print available directions
    directions_in_room = rooms[currentRoom].keys()
    lst_directions = list(directions_in_room)
    print("The available directions are: "+str(lst_directions) )

    #print player's current inventory
    print('Inventory ' + str(inventory) )   
    #print element if any
    if rooms[currentRoom]['element']:
        print ('You see a ' + rooms[currentRoom]['element'])
    print ('-------------------')

inventory=[]

#a dictionary linking one room to the other
rooms={
    'Parlour':{
        'south':'Kitchen',
        'east':'Dining Room',
        'element':'clock',
        'north':'Library'
    },
    'Kitchen':{
        'north':'Parlour',
        'east':'Garage',
        'element':'burger'
    },
    'Dining Room':{
        'west':'Parlour',
        'south':'Garage',
        'element':'flowers'
    },
    'Library':{
        'south':'Parlour',
        'element':'books'
    },
    'Garage':{
        'south':'Dining Room',
        'west':'Kitchen',
        'element':'car'
    }
}


#start player in the parlour
currentRoom = 'Parlour'

showInstructions()

Name = input('My name is Bessem. What is your name:')
print('Welcome ' + Name)

while True:
    showstatus()

    available_rooms = rooms.keys()
    #convert dictlist to list inorder to use choice
    rooms_present = list(available_rooms)
    #choose a random room where the monster would be kept
    monster_room = random.choice(rooms_present)
    #keep the monster there
    rooms[monster_room]['element'] = 'monster'


    move = ''
    while move == '':  
        move = input('>')
    
    move = move.lower().split()

    #defining game over
    if rooms[currentRoom]['element'] == 'monster':
        print("The monster has gotten you...GAME OVER!")
        break
            
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
        #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print("You can't go that way!")

#if they type 'get' first
    if move[0] == 'get' :
        #check that element has not yet been gotten
        #if not rooms[currentRoom]['element']
        #checking if the room contains an element, and the element is the one they want to get
        if "element" in rooms[currentRoom] and move[1] in rooms[currentRoom]['element']:
                #add the element to their inventory
            inventory += [move[1]]
                #display a helpful message
            print(move[1] + ' has been gotten!')
                #delete the element from the room
            rooms[currentRoom]['element'] = None
                #otherwise, if the element isn't there to get
        else:
        #tell them they can't get it
            print("Can't get " + move[1] + '!')

#defining win
    if len(inventory) >= 3:  
        print('CONGRATULATIONS. You have survived the path!')
