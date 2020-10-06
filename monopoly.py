'''
Aim around noon Oct 5.
1. Select token 
2. each player select $1500, one as banker. manage propoties, houses, hotels. 
3. objective: be the wealthiest person among the players
4. Game start: each player rolls 2 dizes.
    4.1 land on proproties: if not owned: if Bought, elif auction: all players play bids. Else owned: pay Rent
        4.1.1. buy properties on land
        4.1.2. Sell properties 
    4.2 land on the chance/community chest : multiple scenerios 
    4.3 land on tax: pay tax
    4.4 jail space, free parking: nothing happens
    4.5 go to jail: goes to jail. 
        3 ways to get out: rolls same numbers in dizes, get "get out if jail" in chance or community chest, or pay $50 dollars to bank. 
    4.6 pass the go (start): collect/pay $200 dollars to banker
    4.7. if rolls the same doze: rolls 2nd time
'''

print ("welcome to Monopoly, please insert # of players.") 
#hasn't define players yet

import random

def roll2dize ():
    
    dize1 = random.randint(1,6)
    dize2 = random.randint(1,6)

    print ("Dize 1:",dize1,";Dize2:",dize2)
    print ("Please move", dize1+dize2, "steps.")

    if dize1 == dize2:
        print ("Hooray!! It's double! You got extra steps! Please roll again!")
        # input ("Press enter to roll again.")

#assume 10*10 square, 36 stops in total
nsquares = 36

nrolls = 5
current_position= 0
for i in range (5):    #set rolls
    total_steps = dize1+dize2
    current_position = current_position + total_steps




