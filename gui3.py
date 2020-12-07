import random
import math
import sys


class Player:
    def __init__(self,name,boardpos,money,jailcards,jailtime,droll,piece,doublesacc,user):



        self.name = str(name)
        self.boardpos = int(boardpos)
        self.money = int(money)
        self.proplist = [[],[],[],[],[],[],[],[]]
        self.raillist = []
        self.utlist = []
        self.jailcards = int(jailcards)
        self.jailtime = int(jailtime)
        self.droll = int(droll)
        self.piece = piece
        self.doublesacc = int(doublesacc)
        self.user = int(user)
    def addproperty(self,newprop):
        newprop.owner = self.name
        self.money = self.money - newprop.cost
        gotprop = 0
        while gotprop == 0:
            if isinstance(newprop,Property):
                if newprop.color == "darkblue":
                    addindex = 0
                if newprop.color == "green":
                    addindex = 1
                if newprop.color == "yellow":
                    addindex = 2
                if newprop.color == "red":
                    addindex = 3
                if newprop.color == "orange":
                    addindex = 4
                if newprop.color == "pink":
                    addindex = 5
                if newprop.color == "lightblue":
                    addindex = 6
                if newprop.color == "purple":
                    addindex = 7

                self.proplist[addindex].append(newprop)
                gotprop = 1

class Board:
   def __init__(self,players,playerpiece):

        self.playerlist = []

        freecharacters = ["Horse","Wheel","Battleship","Racecar","Old Shoe","Iron","Terrier","Wheelbarrow","Thimble","Top Hat"]
        for piece in freecharacters:
            if playerpiece == piece:
                freecharacters.remove(piece)
        user = Player("USER PLAYER",0,1500,0,0,0,playerpiece,0,1)
        self.playerlist.append(user)
        for i in range(1,int(players)+1):
            playernum = i+1
            comppiece = random.choice(freecharacters)
            freecharacters.remove(comppiece)
            print(str(comppiece))
            newplayer = Player(str("COMP"+str(playernum)),0,1500,0,0,0,comppiece,0,0)
            self.playerlist.append(newplayer)



    #for colorlist in self.proplist:
        #if len(colorlist) == 2:
            #for prop in colorlist:
                #if prop.color == "purple":
                  #colorlist.append("monopoly")
                  #break
                #if prop.color == "darkblue":
                  #colorlist.append("monopoly")
                  #break
        #if len(colorlist) == 3:
            #if "monopoly" not in colorlist:
               #colorlist.append("monopoly")
               #break"






def __init__(self,name,boardpos,money,jailcards,jailtime,droll,piece,doublesacc,user):
      
      
     
      self.boardlist = []

      gospace = Freespace("PASS GO","freespace",1)
      self.boardlist.append(gospace)
      medit = Property("Mediterranean Ave.","property",2,60,50,30,2,10,30,90,160,250,"bank","purple",0)
      self.boardlist.append(medit)
      cc1 = Communitychestspace("Community Chest","communitychestspace",3)
      self.boardlist.append(cc1)
      baltic = Property("Baltic Ave.","property",4,60,50,30,4,20,60,180,320,450,"bank","purple",0)
      self.boardlist.append(baltic)
      inctax = Taxspace("Income Tax","taxspace",5,-200)
      self.boardlist.append(inctax)
      r1 = Railroad("Reading Railroad","railroad",6,"bank")
      self.boardlist.append(r1)
      oriental = Property("Oriental Ave.","property",7,100,50,50,6,30,90,270,400,550,"bank","lightblue",0)
      self.boardlist.append(oriental)
      chance1 = Chancespace("Chance","chancespace",8)
      self.boardlist.append(chance1)
      vermont = Property("Vermont Ave.","property",9,100,50,50,6,30,90,270,400,550,"bank","lightblue",0)
      self.boardlist.append(vermont)
      connave = Property("Connecticut Ave.","property",10,120,50,60,8,40,100,300,450,600,"bank","lightblue",0)
      self.boardlist.append(connave)
      jailspace = Freespace("Jail","freespace",11)
      self.boardlist.append(jailspace)
      stchar = Property("St. Charles Place","property",12,140,100,70,10,50,150,450,625,750,"bank","pink",0)
      self.boardlist.append(stchar)
      ut1 = Utility("Electric Company","utility",13,"bank")
      self.boardlist.append(ut1)
      states = Property("States Ave.","property",14,140,100,70,10,50,150,450,625,750,"bank","pink",0)
      self.boardlist.append(states)
      virginia = Property("Virginia Ave.","property",15,160,100,80,12,60,180,500,700,900,"bank","pink",0)
      self.boardlist.append(virginia)
      r2 = Railroad("Pennsylvania Railroad","railroad",16,"bank")
      self.boardlist.append(r2)
      stjames = Property("St. James Place","property",17,180,100,90,14,70,200,550,750,950,"bank","orange",0)
      self.boardlist.append(stjames)
      cc2 = Communitychestspace("Community Chest","communitychestspace",18)
      self.boardlist.append(cc2)
      tennessee = Property("Tennessee Ave.","property",19,180,100,90,14,70,200,550,750,950,"bank","orange",0)
      self.boardlist.append(tennessee)
      newyork = Property("New York Ave.","property",20,200,100,100,16,80,200,600,800,1000,"bank","orange",0)
      self.boardlist.append(newyork)
      freepark = Freespace("Free Parking","freespace",21)
      self.boardlist.append(freepark)
      kentucky = Property("Kentucky Ave.","property",22,220,150,110,18,90,250,700,875,1050,"bank","red",0)
      self.boardlist.append(kentucky)
      chance2 = Chancespace("Chance","chancespace",23)
      self.boardlist.append(chance2)
      indiana = Property("Indiana Ave.","property",24,220,150,110,18,90,250,700,875,1050,"bank","red",0)
      self.boardlist.append(indiana)
      illinois = Property("Illinois Ave.","property",25,240,150,120,20,100,300,750,925,1100,"bank","red",0)
      self.boardlist.append(illinois)
      r3 = Railroad("B&O Railroad","railroad",26,"bank")
      self.boardlist.append(r3)
      atlantic = Property("Atlantic Ave.","property",27,260,150,130,22,110,330,800,975,1150,"bank","yellow",0)
      self.boardlist.append(atlantic)
      ventnor = Property("Ventnor Ave.","property",28,260,150,130,22,110,330,800,975,1150,"bank","yellow",0)
      self.boardlist.append(ventnor)
      ut2 = Utility("Water Works","utility",29,"bank")
      self.boardlist.append(ut2)
      marvin = Property("Marvin Gardens","property",30,280,150,140,24,120,360,850,1025,1200,"bank","yellow",0)
      self.boardlist.append(marvin)
      gojail = Gotojailspace("Go To Jail","gotojailspace",31)
      self.boardlist.append(gojail)
      pacific = Property("Pacific Ave.","property",32,300,200,150,26,130,390,900,1100,1275,"bank","green",0)
      self.boardlist.append(pacific)
      ncarol = Property("North Carolina Ave.","property",33,300,200,150,26,130,390,900,1100,1275,"bank","green",0)
      self.boardlist.append(ncarol)
      cc3 = Communitychestspace("Community Chest","communitychestspace",34)
      self.boardlist.append(cc3)
      pennave = Property("Pennsylvania Ave.","property",35,320,200,160,28,150,450,1000,1200,1400,"bank","green",0)
      self.boardlist.append(pennave)
      r4 = Railroad("Short Line","railroad",36,"bank")
      self.boardlist.append(r4)
      chance3 = Chancespace("Chance","chancespace",37)
      self.boardlist.append(chance3)
      parkplace = Property("Park Place","property",38,350,200,175,35,175,500,1100,1300,1500,"bank","darkblue",0)
      self.boardlist.append(parkplace)
      luxtax = Taxspace("Luxury Tax","taxspace",39,75)
      self.boardlist.append(luxtax)
      boardwalk = Property("Boardwalk","property",40,400,200,200,50,200,600,1400,1700,2000,"bank","darkblue",0)
      self.boardlist.append(boardwalk)


def playermove(self,player,movenum,warp):
      
        if player.droll == 1:
            player.doublesacc += 1
        if player.droll == 0:
            player.doublesacc = 0
        if player.doublesacc == 3:
            player.boardpos = 11
            player.jailime = 3
            print(str(player.name) + " has rolled doubles three times in a row. " + str(player.name) + " is now in JAIL.")
        else:
            newspot = int(movenum) + player.boardpos
            if warp == 1:
                newspot = int(movenum)
                if player.boardpos > newspot:
                    player.money += int(200)
                    print(player.name + " has passed go and collects $200.")
                    player.boardpos = newspot
            if newspot > 39:
                newspot += -39
                player.money += int(200)
                print(player.name + " has passed go and collects $200.")
            player.boardpos = newspot
            for space in self.boardlist:
                if self.boardlist.index(space) == player.boardpos:
                    currspace = space
                break
            print(player.name + " has landed on " + currspace.name + ".")




        if isinstance(currspace,Property):
            if currspace.owner == "bank":                           
               if player.user == 0:                                 
                  for colorlist in player.proplist:
                     for prop in colorlist:
                        if isinstance(prop,str):            
                           continue                         
                        if isinstance(prop,Property):       
                           if prop.color == currspace.color:          
                              if player.money >= currspace.cost:
                                 player.addproperty(currspace)
                                 print(str(player.name) + " has purchased " + str(currspace.name) + " for $" + str(currspace.cost) + ".")
                                 break
                  if currspace.owner == "bank":
                     if player.money >= currspace.cost:
                        buychoice = random.randint(0,1)
                        if buychoice == 1:
                           player.addproperty(currspace)
                           print(str(player.name) + " has purchased " + str(currspace.name) + " for $" + str(currspace.cost) + ".")
               if player.user == 1:
                  if player.money >= currspace.cost:                 
                     buywhile = 0
                     while buywhile == 0:
                        choice = input("NOBODY OWNS " + str(currspace.name) + ". WOULD YOU LIKE TO BUY IT? TYPE Y OR N.")
                        if choice == "Y":
                           player.addproperty(currspace)
                           print("You have purchased " + str(currspace.name) + " for $" + str(currspace.cost) + ".")
                           buywhile = 1
                        if choice == "N":
                           buywhile = 1
                        else:
                           print("Invalid input. Available answers are Y (yes) or N (no).")   

                  else:
                     print("YOU DON'T HAVE ENOUGH MONEY TO PURCHACE THIS PROPERTY. TRY AGAIN LATER problem1")
            elif currspace.owner == player.name:
               task = "do nothing"
            else:
               for person in self.playerlist:              
                  if person.name == currspace.owner:
                     propowner = person
               hasmonopoly = 0                               
               for colorlist in propowner.proplist:
                  if colorlist:
                     for prop in colorlist:
                        if prop.color == currspace.color:
                           if "monopoly" in colorlist:
                              hasmonopoly = 1
                              break
               if hasmonopoly == 1:
                  if currspace.houses == 0:
                     payout = 2*int(currspace.rent)
                  elif currspace.houses == 1:
                     payout = int(currspace.h1)
                  elif currspace.houses == 2:
                     payout = int(currspace.h2)
                  elif currspace.houses == 3:
                     payout = int(currspace.h3)
                  elif currspace.houses == 4:
                     payout = int(currspace.h4)
                  elif currspace.houses == 5:
                     payout = int(currspace.h5)
                  if player.money <= payout:
                     propowner.money += player.money
                     self.playerlose(player)
                     print("By landing on " + str(propowner.name) + "'s " + str(currspace.name) + " with insufficient funds, " + str(player.name) + " has lost the game.")
                  else:
                     player.money += -payout
                     propowner.money += payout
                     print(str(player.name) + " has landed on " + str(propowner.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")
               else:
                  payout = int(currspace.rent)
                  if player.money <= payout:
                     propowner.money += player.money
                     self.playerlose(player)
                     print("By landing on " + str(propowner.name) + "'s " + str(currspace.name) + " with insufficient funds, " + str(player.name) + " has lost the game.")
                  else:
                     player.money += -payout
                     propowner.money += payout
                     print(str(player.name) + " has landed on " + str(propowner.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")
                  
            if isinstance(currspace,Railroad):
                if currspace.owner == "bank":                        
                    if player.money >= currspace.cost:
                        if player.user == 0:                              
                            if len(player.raillist) >= 1:
                                player.addproperty(currspace)
                                print(player.name + " has purchased " + currspace.name + " for $" + str(currspace.cost) + ".")
                            else:
                                buychoice = random.randint(0,1)
                                if buychoice == 1:
                                    player.addproperty(currspace)
                                    print(player.name + " has purchased " + str(currspace.name) + " for $" + str(currspace.cost) + ".")         
                    else:
                        railwhile = 0
                        while railwhile == 0:
                            choice = input("NOBODY OWNS " + str(currspace.name) + ". WOULD YOU LIKE TO BUY IT? TYPE Y OR N.")
                            if choice == "Y":
                                player.addproperty(currspace)
                                railwhile = 1
                            elif choice == "N":
                                railwhile = 1
                            else:
                                print("Invalid input. Available answers are Y (yes) or N (no).")
                else:
                    print("YOU DON'T HAVE ENOUGH MONEY TO PURCHACE THIS PROPERTY. TRY AGAIN LATER")
                if currspace.owner == player.name:
                    task = "do nothing"
                else:
                    for person in self.playerlist:                    
                        if person.name == currspace.owner:
                            propowner = person
                if len(propowner.raillist) == 1:
                    payout = int(currspace.rr1)
                elif len(propowner.raillist) == 2:
                    payout = int(currspace.rr2)
                elif len(propowner.raillist) == 3:
                    payout = int(currspace.rr3)
                elif len(propowner.raillist) == 4:
                    payout = int(currspace.rr4)
                if player.money <= payout:
                    propowner.money += player.money
                    self.playerlose(player)
                    print("By landing on " + str(propowner.name) + "'s " + str(currspace.name) + " with insufficient funds, " + str(player.name) + " has lost the game.")
                else:
                    player.money += -payout
                    propowner.money += payout
                    print(str(player.name) + " has landed on " + str(propowner.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")


            if isinstance(currspace,Utility):
                if currspace.owner == "bank":                          
                    if player.money >= currspace.cost:
                        if player.user == 0:                               
                            if len(player.utlist) >= 1:
                                player.addproperty(currspace)
                                print(player.name + " has purchased " + currspace.name + " for $" + str(currspace.cost) + ".")
                            else:
                                buychoice = random.randint(0,1)
                                if buychoice == 1:
                                    player.addproperty(currspace)
                                    print(player.name + " has purchased " + currspace.name + " for $" + str(currspace.cost) + ".")          
                        elif player.user == 1:
                            utwhile = 0
                            while utwhile == 0:
                                choice = input("NOBODY OWNS " + str(currspace.name) + ". WOULD YOU LIKE TO BUY IT? TYPE Y OR N.")
                                if choice == "Y":
                                    player.addproperty(currspace)
                                    utwhile = 1
                                elif choice == "N":
                                    utwhile = 1
                                else:
                                    print("Invalid input. Available answers are Y (yes) or N (no).")
                else:
                    print("YOU DON'T HAVE ENOUGH MONEY TO PURCHACE THIS PROPERTY. TRY AGAIN LATER")
                if currspace.owner == player.name:
                    task = "do nothing"
                else:
                    for person in self.playerlist:                     
                        if person.name == currspace.owner:
                            propowner = person
                    if len(propowner.utlist) == 1:
                        payout = int(currspace.u1)
                    elif len(propowner.utlist) == 2:
                        payout = int(currspace.u2)
                    if player.money <= payout:
                        propowner.money += player.money
                        self.playerlose(player)
                        print("By landing on " + str(propowner.name) + "'s " + str(currspace.name) + " with insufficient funds, " + str(player.name) + " has lost the game.")
                    else:
                        player.money += -payout
                        propowner.money += payout
                        print(str(player.name) + " has landed on " + str(propowner.name) + "'s " + str(currspace.name) + " and pays " + str(payout) + ".")

def PREMOVE(self,player):
      if player.jailtime > 0:
         if player.user == 0:
            if player.jailcards >= 0:
               player.jailcards += -1
               player.jailtime = 0
            if player.money >= 50:
               player.money += 50
               player.jailtime = 0
            else:
               print(player.name + " attempts to roll doubles to get out of jail.")
               die1 = random.randint(1,6)
               die2 = random.randint(1,6)
               print("die 1 roll: " + str(die1))
               print("die 2 roll: " + str(die2))



def main():
   print("WELCOME TO")
   print(" MONOPOLY MASTERS' MONOPOLY BONANZA" )
   firstwhile = 0
   while firstwhile == 0:
      numplay = int(input("Please enter the number of computer players you want to play against."))
      if numplay > 0:
         firstwhile = 1
      else:
         print("Invalid input. Please select one or more players to play against.  ")
   playname = str("USER PLAYER")
   gameboard = Board(numplay,playname)
   playgame = 1
   while playgame == 1:
      for player in gameboard.playerlist:
         if len(gameboard.playerlist) == 1:
            for player in gameboard.playerlist:
               print(player.name + " WINS!")
            playgame = 0   
         print(player.name + "'s turn!")
         if player.jailtime > 0:
            print(player.name + " is in JAIL.")
         gameboard.PREMOVE(player)
         print(player.name + " rolls the dice!")
         die1 = random.randint(1,6)
         die2 = random.randint(1,6)
         print("die 1 roll:      " + str(die1))
         print("die 2 roll:      " + str(die2))
         if die1 == die2:
            player.droll = 1
         else:
            player.droll = 0
         gameboard.playermove(player,int(die1+die2),0)
         print(" ")
         print(" ")
main()  
