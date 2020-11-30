import random

print("Developed by Monopoly Masters team \n")
# print("""[ This file allows a single player to start at the Go space and move around
# the board as he or she randomnly rolls a pair of dice.  It utlizes random object in
# rolling the pair of dice and a loop to continue the process until the user decides 
# to end the experience. ]\n""")

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


def roll2dize():    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total_steps = dice1+dice2
    print ("Dice1:",dice1,"; Dice2:",dice2)
    return total_steps


current = 0
dice1 = dice2 = total = 0
doubles = 0
rolls = 0
print("Welcome to the Monopoly Python Board.  You are currently on the Go (Collect $200).")

print('Please enter player numbers:')
player_num = input()

print('Welcome ! Please enter player names:')

players = [] #list of players

for i in range(1,int(player_num)+1):
    player_names = input()         #type players name
    players.append(player_names)   #add players in players[]
 
player_count = {}
for p in players:
    p = p+'count'
    player_count[p] = 0

listtostr = ', '.join([str(elem) for elem in players])

print('Hello '+ listtostr + ' !')
roll_dices = input ("Press the enter key to roll the dice (enter x to end):")

while (roll_dices.upper() != "X"): 
    player_turn = input('Whose turn is it, please enter your name: ')
    if player_turn in players:
        print("Here is the dice results")
        dice_count = roll2dize()
        player_turn = player_turn+'count'
        player_count[player_turn] =  player_count[player_turn] +dice_count
        Space = boardspaces[player_count[player_turn]]  
        print('\nYou rolled for a total of '+ str(dice_count) +'.  You\'re at '+ Space)  #print the player steps and current location
        print(player_count)
        roll_dices = input("Press the enter key to roll the dice again (enter x to end:) ")





