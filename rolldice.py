import random

print("Developed by Monopoly Masters team \n")
print("""This file allows a single player to start at the Go space and move around
the board as he or she randomnly rolls a pair of dice.  It utlizes random object in
rolling the pair of dice and a loop to continue the process until the user decides 
to end the experience. ]\n""")

# Create the board spaces based upon link: 
# https://en.wikipedia.org/wiki/Template:Monopoly_board_layout
boardspaces = ["Go (Collect $200)", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax", 
               "Reading Railroad", "Oriental Avenue", "Chance", "Vermont Ave", "Connecticut Ave", 
               "Just Visiting (Jail)", "St. Charles Place", "Electric Company", "States Ave", "Virginia Ave", 
               "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Ave", "New York Ave", 
               "Free Parking", "Kentucky Ave", "Chance", "Indiana Ave", "Illinois Ave", 
               "B&O Railroad", "Atlantic Ave", "Ventnor Ave", "Water Works", "Marvin Gardens", 
               " Go to Jail", "Pacific Ave", "North Carolina Ave", "Community Chest", "Pennsylvania Ave", 
               " Short Line Railroad", "Chance", "Park Place", "Luxury Tax", "Boardwalk!"]

current = 0
die1 = die2 = total = 0
doubles = 0
rolls = 0
print("Welcome to the Monopoly Python Board.  You are currently on the Go (Collect $200).")
roll_dices = input ("Press the Enter key to roll the dice (enter x to end):")

while (roll_dices.upper() != "X"): 
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    rolls += 1
    current = (current + total) % 40 # add total roll to current location and use modulus to
    mySpace = boardspaces[current]
    print('\nYou rolled a {0} and {1} for a total of {2}.  You\'re at {3}.'.format(die1, die2, total, mySpace))
    roll_dices = input("Press the enter key to roll the dice again (enter x to end:) ")

print("\nThank you for playing...you rolled", rolls, "times.\n")

# 
