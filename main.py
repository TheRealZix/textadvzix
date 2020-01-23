# text adventure game
# made by zix

from Spot import Spot
from User import User

# define constants
HELP = """
 * * * * * * * * * * 
 
 view [direction]
    Describes what you see in the specified direction.
    [direction]: n, s, e, w, north, south, east, west
 
 go [direction]
    Travels in the specified direction.
    [direction]: n, s, e, w, north, south, east, west
    
 * * * * * * * * * * 
"""

MAP = dict()


# returns a formatted string for coordinates
def coords(x, y):
    # e.g. coords(-3, 42) returns the string "-3x42"
    return str(x) + "x" + str(y)


# creates a new spot on the map
def create_spot(x, y):
    MAP[coords(x, y)] = Spot(x, y)


# moves the user to the specified coordinates on the map
def move(x, y):
    # checks if spot exists yet on the map; if not, it creates the spot
    if coords(x, y) not in MAP:

        # create the new spot
        create_spot(x, y)

    # update the user's current coords
    current_coords = coords(x, y)

    # check if surrounding spots exist on the map; if not, create these spots
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if coords(x + dx, y + dy) not in MAP:
                create_spot(x + dx, y + dy)


# prints a visual representation of the map in the surrounding area of the user
def print_map():
    # the column width is the visually widest X value surrounding the user
    column_width = max(str(user.x - 1), str(user.x), str(user.x + 1))

    # the row width is based off the column width
    row_width = 


# asks for user input and processes the command given
def take_input():
    user_input = str(input(" > ")).lower()  # collect user command and make it lowercase

    # lists commands the user can give
    if user_input == "help":
        print(HELP)

    # prints a visual representation of the current map


    # temporary debug command which shows variable values and such
    if user_input == "debug":
        print(MAP)

    # moves the player in the specified direction if possible
    elif user_input[:3] == "go ":
        if user_input[3:] in "north":
            if MAP[user.coords].passable_north:
                move(user.x, user.y + 1)
            else:
                print("Sorry, you can't go that way!")
        elif user_input[3:] in "east":
            if MAP[user.coords].passable_east:
                move(user.x + 1, user.y)
            else:
                print("Sorry, you can't go that way!")
        elif user_input[3:] in "south":
            if MAP[user.coords].passable_south:
                move(user.x, user.y - 1)
            else:
                print("Sorry, you can't go that way!")
        elif user_input[3:] in "west":
            if MAP[user.coords].passable_west:
                move(user.x - 1, user.y)
            else:
                print("Sorry, you can't go that way!")
        else:
            print(user_input[3:] + " is not a valid direction.")

    # describes to the user what is in the specified direction
    elif user_input[:5] == "view ":
        if user_input[5] in "nsew":
            view = MAP[user.coords]["view"][user_input[5]]
            print(view)
        else:
            print(user_input[5:], "is not a valid direction.")

    # inform the user that they have provided an invalid command
    else:
        print(user_input, "is not a valid command. Type 'help' for a list of commands.")


# greet the user and start the game
if __name__ == "__main__":
    username = input("Please enter your name: ")
    user = User(username)
    print("Welcome, %s." % user.name)
    print("You're in the middle of the forest. Type 'help' for a list of commands.")

    move(0, 0)
    # enter an infinite loop
    while True:
        take_input()
