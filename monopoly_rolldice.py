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

property = {"Mediterranean Ave":60, "Baltic Ave":60,  
              "Oriental Avenue":100, "Vermont Ave":100, "Connecticut Ave":120, 
               "St. Charles Place":120, "States Ave":140, "Virginia Ave":160, 
            "St. James Place":180, "Tennessee Ave":180, "New York Ave":200, 
            "Kentucky Ave":220, "Indiana Ave":220, "Illinois Ave":240, 
               "Atlantic Ave":260, "Ventnor Ave":260, "Marvin Gardens":280, 
               "Pacific Ave":300, "North Carolina Ave":300, "Pennsylvania Ave":320, 
               "Park Place":350, "Boardwalk!":400}

def property_list(property):
    list =[]
    for key in property.keys:
        list.append(key)
    return list

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
print("Welcome to the Monopoly Python Board. You are currently on the Go (Collect $200).")

print('Please enter player numbers:')
player_num = input()

print('Welcome ! Please enter player names:')

players = [] #list of players

for i in range(1,int(player_num)+1):
    player_names = input()         #type players name
    players.append(player_names)   #add players in players[]
 
player_count = {}
for p in players:
    p = p+'_count'
    player_count[p] = 0

player_balance = {}
for p in players:
    p = p + '_balance'
    player_balance [p] = 1500

listtostr = ', '.join([str(elem) for elem in players])

print('Hello '+ listtostr + ' !')
roll_dices = input ("Press the enter key to roll the dice (enter x to end):")

while (roll_dices.upper() != "X"): 
    player_turn = input('Whose turn is it, please enter your name: ')
    if player_turn in players:
        print("Here is the dice results")
        dice_count = roll2dize()
        player_turn = player_turn+'_count'
        player_count[player_turn] =  player_count[player_turn] +dice_count
        Space = boardspaces[player_count[player_turn]]  
        print('\nYou rolled for a total of '+ str(dice_count) +'.  You\'re at '+ Space)  #print the player steps and current location
        print(player_count)
        print(player_balance)
        if player_count[player_turn] in [1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39]:  
            # Space in property_list(property): doesn't work
            buy_or_not = input('Would you like to buy '+ Space +' or not? Type yes or no ')  
            if buy_or_not.lower() == 'yes':
                print ('Pay the property to the bank please.') 
                player_balance[p] = player_balance[p] - property[Space] # Q: assign the ownership?
                print(player_balance)
            else:
                pass
        # elif player_count[player_turn] in [4,5,12,25,28,35,38]:
        #     print ('Pay the tolls to the bank please.') 
        #     player_balance[p] = player_balance[p] - property[Space] #pass by railway and water pay tolls
        else: 
            pass
        roll_dices = input("Press the enter key to roll the dice again (enter x to end:) ")





