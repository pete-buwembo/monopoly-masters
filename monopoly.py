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
    4.7. if rolls the same doze: rolls 2nd time/double steps
'''

import random
game = True
total_steps=0
position= 0
nsquares = 40
round = 1

#assume  40 stops in total
while game == True:

    dize1 = random.randint(1,6)
    dize2 = random.randint(1,6)
    total_steps = dize1+dize2

    print ("Dize 1:",dize1,"; Dize2:",dize2)

    #new position after each round
    position = position + total_steps

    if position > 39:
        position = position - 40
        round = round + 1
        # print("You have entered ", round, "round.")
    
    print ("Please move", dize1+dize2, "steps,","to position", position)

    # got double steps when dize1 = dize2
    if dize1 == dize2:
        position = position +total_steps
        print ("Hooray!! It's double! You got double steps!")
        game == False
   
    # Position 30 = Be in jail
    if position == 30:
        print ("You have been sent to jail in round", round,".")
        game == False
        break





