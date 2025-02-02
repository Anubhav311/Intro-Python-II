from room import Room
from player import Player
from item import Item

# Declare all the rooms

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

rock = Item("Rock", "this is a rock")
pencil = Item("Pencil", "this is a pencil")
sandwich = Item("Sandwich", "this is delicious sandwich")

player = Player("Player 1", room["outside"])

player.items.append(rock)
room['outside'].items.append(pencil)
room['outside'].items.append(sandwich)

current_room = player.current_room

print(current_room)

valid_directions = ["n", "s", "e", "w"]

while True:
    cmd = input("provide direction e/w/n/s -> ")

    if cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else:
        print("I did not recognise that command")




# while True:
#     print("room name: ", getattr(player.current_room, "name"))
#     print("description: ", player.current_room.description, "\n")

#     direction = input("provide direction e/w/n/s -> ") 

#     if direction == "q":
#         player.current_room = room["outside"]
#         print("Adios...!!!", "\n")
#         break

#     elif direction != "e" and direction != "w" and direction != "n" and direction != "s":
#         print("please provide a valid input", "\n")

#     elif getattr(player.current_room, f"{direction}_to") == "nope":
#         print("Sorry! there's no room here.", "\n")

#     else:
#         player.current_room = getattr(player.current_room, f"{direction}_to")



