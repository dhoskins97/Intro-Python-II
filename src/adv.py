from room import Room
from player import Player
from item import Item


# Declare all the rooms and items

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'sword': Item("Rusty Sword", "A rusty blade originally found leaning against the entrance of the mysterious cave."),
    'shield': Item("Dented Buckler", "A brightly-polished piece of bronze headgear."),
    'helmet': Item("Burnished Helmet", "A brightly-polished piece of bronze headgear."),
    'bplate': Item("Shiny Breastplate", "A well-made piece of armor to protect one's torso."),
    'greaves': Item("Golden Greaves", "A pair of metal plates fitted to protect the lower-legs."),
    'pauldrons': Item("Old Pauldrons", "A piece of armor to sit on the shoulders, made of old leather."),
    'gold': Item("Sack of Coins", "Marvelous money!")
}

# Place items.

room['outside'].inv.append(item['sword'])

room['foyer'].inv.append(item['shield'])
room['foyer'].inv.append(item['helmet'])

room['narrow'].inv.append(item['bplate'])
room['narrow'].inv.append(item['greaves'])
room['narrow'].inv.append(item['pauldrons'])

room['treasure'].inv.append(item['gold'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player("Adventurer", room['outside'])

while True:
    print(f'You are currently in {player.location.name}, for a list of commands, type \'help\'')

    prompt = input("What will you do? ")

    if prompt == "help":
        print("Type 'look' to look around.")
        print("Type 'move' to go to a different room, and then north, south, east, or west to move in that corresponding direction.")
        print("Type 'search' to search your location for items.")
        print("Type 'take' to take an item, and then the name of that item you want to take.")
        print("Type 'look at' to look at an item, and then the name of the item you want to look at.")
        print("Type 'check inv' to see what is in your inventory.")
    
    elif prompt == "look":
        print(player.location.desc)
    
    elif prompt == "move":
        
        dir = input("What direction do you move in? ")
        
        if dir == "north":
            if player.location.n_to is None:
                print("You cannot go that way!")
            else:
                player.location = player.location.n_to
    
        elif dir == "south":
            if player.location.s_to is None:
                print("You cannot go that way!")
            else:
                player.location = player.location.s_to
    
        elif dir == "east":
            if player.location.e_to is None:
                print("You cannot go that way!")
            else:
                player.location = player.location.e_to
    
        elif dir == "west":
            if player.location.w_to is None:
                print("You cannot go that way!")
            else:
                player.location = player.location.w_to
    
        else:
           print("Invalid direction.")

    elif prompt == "search":
        retStr = "You find:"
        for item in player.location.inv:
            retStr += f" {item.__str__()}, "
        print(retStr)

    elif prompt == "take":

        takeWhat = input("Take what? ")
        
        for item in player.location.inv:
            if takeWhat == item.name:
                player.location.inv.remove(item)
                player.inv.append(item)
                print(f"You take the {item.name}")
            else:
                print("That isn't here!")

    elif prompt == "look at":

        lookWhat = input("Look at what? ")

        for item in player.location.inv:
            if lookWhat == item.name:
                print(item.desc)
            else:
                print("That isn't here!")
    
    elif prompt == "check inv":
        retStr = "You have: "
        for item in player.inv:
            retStr += f" {item.__str__()}, "
        print(retStr)

    else:
        print("Invalid command.")



