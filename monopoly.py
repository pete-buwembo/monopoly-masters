#https://www.youtube.com/watch?v=xqDPS091hIQ
#image:https://www.google.com/search?q=monopoly&sxsrf=ALeKk03qKqRp_Swt1XUGKPvtmaw5pVh8DQ:1601958218825&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiFrM-0j5_sAhWqFTQIHeu2AXkQ_AUoAXoECBcQAw&biw=1309&bih=746#imgrc=i4faNggT28mDaM

import random
game = True
total_steps=0
position= 0
nsquares = 40
round = 1

def take_turn():
    player_turn = input('Whose turn is it, please enter your name ')
    if player_turn in players:
        print("Here is the dice results")
        dice_count = roll2dize()
        player_turn = player_turn+'count'
        player_count[player_turn] =  player_count[player_turn] +dice_count
        print(player_count)

def roll2dize():    

    dize1 = random.randint(1,6)
    dize2 = random.randint(1,6)
   
    total_steps = dize1+dize2
    print ("Dize1:",dize1,"; Dize2:",dize2)
    return total_steps

    # position = position + total_steps      #new position after each round

#create input based on the number enter

print('Enter player numbers:')
player_num = input()

print('Welcome ! Please enter player names:')

players = []

for i in range(1,int(player_num)+1):
    player_names = input()
    players.append(player_names)  #Q: get rid of []? necessary?

 
player_count = {}
for p in players:
    p = p+'count'
    player_count[p] = 0

print('Welcome! ', players) 
print(player_count)
take_turn()
position = position + total_steps      #new position after each round

#assume  40 stops in total
#Q4: seperate each players' dizes rolls? try use class or dictionary
# while game == True:



    # player_positions ={}
    # for i in players:  
    #     player_
    #     player_positions['player_%s' % i]=[]
        #The %s signifies that you want to add a string value into a string


    # if position > 39:
    #     position = position - 40
    #     round = round + 1
    #     # print("You have entered ", round, "round.")
    
    # print ("Please move", dize1+dize2, "steps,","to position", position)
    # break

    # # got double steps when dize1 = dize2
    # if dize1 == dize2:
    #     position = position +total_steps
    #     print ("Hooray!! It's double! You got double steps!")
    #     game == False
   
    # # Position 30 = Be in jail
    # if position == 30:
    #     print ("You have been sent to jail in round", round,".")
    #     game == False
    #     break

'''
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





