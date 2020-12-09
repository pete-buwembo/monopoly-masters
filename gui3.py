import random
import math
import sys


class SPACE:
   def __init__(self):
      type = space

class Property(SPACE):
   def __init__(self,name,stype,bp,cost,housecost,mortgage,rent,h1,h2,h3,h4,h5,owner,color,houses):
      self.name = name
      self.stype = stype
      self.bp = bp
      self.owner = owner

      self.color = color
      self.cost = int(cost)
      self.housecost = int(housecost)
      self.mortgage = int(mortgage)
      self.rent = int(rent)
      self.h1 = int(h1)
      self.h2 = int(h2)
      self.h3 = int(h3)
      self.h4 = int(h4)
      self.h5 = int(h5)
      self.houses = int(houses)

class Railroad(SPACE):
   def __init__(self,name,stype,bp,owner):
      self.name = name
      self.stype = stype
      self.bp = bp
      self.owner = owner

      self.cost = float(200)
      self.rr1 = float(25)
      self.rr2 = float(50)
      self.rr3 = float(100)
      self.rr4 = float(200)
      self.mortgage = float(100)

class Utility(SPACE):
   def __init__(self,name,stype,bp,owner):
      self.name = name
      self.stype = stype
      self.bp = bp
      self.owner = owner

      self.cost = float(150)
      self.u1 = float(4)
      self.u2 = float(10)
      self.mortgage = float(75)

class Taxspace(SPACE):
   def __init__(self,name,stype,bp,tax):
      self.name = name
      self.stype = stype
      self.bp = bp

      self.tax = tax

class Freespace(SPACE):
   def __init__(self,name,stype,bp):
      self.name = name
      self.stype = stype
      self.bp = bp

      

class Gotojailspace(SPACE):
   def __init__(self,name,stype,bp):
      self.name = name
      self.stype = stype
      self.bp = bp

class Communitychestspace(SPACE):
   def __init__(self,name,stype,bp):
      self.name = name
      self.stype = stype
      self.bp = bp

class Chancespace(SPACE):
   def __init__(self,name,stype,bp):
      self.name = name
      self.stype = stype
      self.bp = bp



class CommunityChestCard:
   def __init__(self,description,move,collect,pay,payperhouse,getoutofjailfree,gotojail,collect50):
      self.description = description
      self.move = int(move)
      self.collect = int(collect)
      self.pay = int(pay)
      self.payperhouse = int(payperhouse)
      self.getoutofjailfree = getoutofjailfree
      self.gotojail = gotojail
      self.collect50 = collect50

class ChanceCard:
   def __init__(self,description,move,collect,pay,payperhouse,getoutofjailfree,gotojail,moveback):
      self.description = description
      self.move = int(move)
      self.collect = int(collect)
      self.pay = int(pay)
      self.payperhouse = int(payperhouse)
      self.getoutofjailfree = getoutofjailfree
      self.gotojail = gotojail
      self.moveback = moveback


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



         if isinstance(newprop,Railroad):
            self.raillist.append(newprop)
            gotprop = 1
         if isinstance(newprop,Utility):
            self.utlist.append(newprop)
            gotprop = 1

      for colorlist in self.proplist:     
         if len(colorlist) == 2:
            for prop in colorlist:
               if prop.color == "purple":
                  colorlist.append("monopoly")
                  break
               if prop.color == "darkblue":
                  colorlist.append("monopoly")
                  break
         if len(colorlist) == 3:
            if "monopoly" not in colorlist:
               colorlist.append("monopoly")
               break



   def buyhouse(self,modprop):
      for colorlist in self.proplist:
         for prop in colorlist:
            if modprop.name == prop.name:
               prop.houses += 1

   def mortgageprop(self,modprop):
      self.money += modprop.mortgage
      modprop.owner = "bank"
      for colorlist in self.proplist:
         for prop in colorlist:
            if modprop.name == prop.name:
               colorlist.remove(prop)
      for rail in raillist:
         if modprop.name == rail.name:
            raillist.remove(rail)
      for ut in utlist:
         if modprop.name == ut.name:
            utlist.remove(ut)
               
            
         
         







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

 #  def __init__(self,name,boardpos,money,jailcards,jailtime,droll,piece,doublesacc,user):
      
      
     
      self.boardlist = []

      gospace = Freespace("PASS GO","freespace",1)
      self.boardlist.append(gospace)
      medit = Property("Mediterranean Ave.","property",2,60,50,30,2,10,30,90,160,250,"bank","purple",0)
      self.boardlist.append(medit)
      cc1 = Communitychestspace("Community Chest","communitychestspace",3)
      self.boardlist.append(cc1)
      baltic = Property("Baltic Ave.","property",4,60,50,30,4,20,60,180,320,450,"bank","purple",0)
      self.boardlist.append(baltic)
      inctax = Taxspace("Income Tax","taxspace",5,200)
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



      self.cclist = []

      ccdesc1 = "GRAND OPERA OPENING. COLLECT $50 FROM EVERY PLAYER"
      c1 = CommunityChestCard(ccdesc1,0,0,0,0,0,0,50)
      self.cclist.append(c1)
      ccdesc2 = "RECEIVE FOR SERVICES $25"
      c2 = CommunityChestCard(ccdesc2,0,10,0,0,0,0,0)
      self.cclist.append(c2)
      ccdesc3 = "ADVANCE TO GO (COLLECT $200) "
      c3 = CommunityChestCard(ccdesc3,1,0,0,0,0,0,0)
      self.cclist.append(c3)
      ccdesc4 = "PAY HOSPITAL $100 "
      c4 = CommunityChestCard(ccdesc3,0,0,100,0,0,0,0)
      self.cclist.append(c4)
      ccdesc5 = "DOCTOR'S FEE. PAY $50 "
      c5 = CommunityChestCard(ccdesc5,0,0,50,0,0,0,0)
      self.cclist.append(c5)


      self.chancelist = []

      cdesc1 = "ADVANCE TO ILLINOIS AVE. IF YOU PASS GO, COLLECT $200.00"
      c1 = ChanceCard(cdesc1,25,0,0,0,0,0,0)
      self.chancelist.append(c1)
      cdesc2 = "YOU ARE ASSESSED FOR STREET REPAIRS. $40.00 PER HOUSE."
      c2 = ChanceCard(cdesc2,0,0,0,40,0,0,0)
      self.chancelist.append(c2)


      random.shuffle(self.playerlist)
      random.shuffle(self.cclist)
      random.shuffle(self.chancelist)


   def playerlose(self,player):
      for item in self.boardlist:
         if isinstance(item,Property):
            if item.owner == player.name:
               item.owner = "bank"
               item.houses = 0
         if isinstance(item,Railroad):
            if item.owner == player.name:
               item.owner = "bank"
               item.houses = 0
         if isinstance(item,Utility):
            if item.owner == player.name:
               item.owner = "bank"
               item.houses = 0

      

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
                           print("Invalid input. Available answers are Y (yes) or N (no).")   #PROBLEM

                  else:
                     print("YOU DON'T HAVE ENOUGH MONEY TO PURCHACE THIS PROPERTY. TRY AGAIN LATER problem1")
            elif currspace.owner == player.name:
               task = "do nothing"
            else:
               for person in self.playerlist:                 # determine property owner
                  if person.name == currspace.owner:
                     propowner = person
               hasmonopoly = 0                                # determine if monopoly
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
            elif currspace.owner == player.name:
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
            elif currspace.owner == player.name:
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



         if isinstance(currspace,Taxspace):
            paytax = currspace.tax
            if player.money <= paytax:
               self.playerlose(player)
               print("With insufficient funds to pay the "+ str(currspace.name) + " of " + str(currspace.tax) + ", " + str(player.name) + " has lost the game.")
            else:
               player.money += -paytax
               print(str(player.name) + " has landed on " + str(currspace.name) + " and pays " + str(paytax) + ".")


         if isinstance(currspace,Freespace):
            print("nothing happens.")


         if isinstance(currspace,Gotojailspace):
            player.boardpos = 11
            player.jailime = 3
            print(str(player.name) + " has landed on " + str(currspace.name) + ". " + str(player.name) + " is now in JAIL.")


         if isinstance(currspace,Communitychestspace):
            self.cclist.append(self.cclist.pop(0))    
            card = self.cclist[-1]
            print("Community Chest!" + str(player.name) + "'s card says: " + str(card.description))
            if card.move > 0:
               self.playermove(player,card.move,1)
            if card.collect > 0:
               player.money += card.collect
            if card.pay > 0:
               player.money += -card.pay
            if card.payperhouse > 0:
               player.money += -card.payperhouse
            if card.getoutofjailfree > 0:
               player.jailcards += 1
            if card.gotojail > 0:
               player.boardpos = 11
               player.jailime = 3
               print(str(player.name) + " is now in JAIL.")
            if card.collect50 > 0:
               for i in self.playerlist:
                  if i != player:
                     if i.money >= 50:
                        i.money += -50
                        player.money += 50
                     else:
                        player.money += i.money
                        i.playerlose()
                        print(i.name + " has insufficient funds to pay the $50, and loses the game.")


         if isinstance(currspace,Chancespace):
            self.chancelist.append(self.chancelist.pop(0))   
            card = self.chancelist[-1]
            print("Chance!" + str(player.name) + "'s card says: " + str(card.description))
            if card.move > 0:
               self.playermove(player,card.move,1)
            if card.collect > 0:
               player.money += card.collect
            if card.pay > 0:
               player.money += -card.pay
            if card.payperhouse > 0:
               player.money += -card.payperhouse
            if card.getoutofjailfree > 0:
               player.jailcards += 1
            if card.gotojail > 0:
               player.boardpos = 11
               player.jailime = 3
               print(str(player.name) + " is now in JAIL.")
            if card.moveback > 0:
               self.playermove(player,int(player.boardpos)-1,1)

         if player.droll == 1:
            print(player.name + " has rolled doubles, and gets to roll again!")
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("die 1 roll: " + str(die1))
            print("die 2 roll: " + str(die2))
            if die1 == die2:
               player.droll = 1
            else:
               player.droll = 0
            self.playermove(player,int(die1+die2),0)
   




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
               if die1 == die2:
                  player.jailtime = 0               

         if player.user == 1:
            print("You are in Jail.")
            if player.jailcards >= 0:
               jcwhile == 0
               while jcwhile == 0:
                  usejc = input("Do you want to use a jailcard to get out? Type Y or N.")
                  if usejc == "Y":
                     player.jailcards += -1
                     player.jailtime = 0
                     jcwhile = 1
                  elif usejc == "N":
                     jcwhile = 1
                  else:
                     print("invalid input. Available answers are YES or NO (make sure caps is on).")

            if player.money >= 50:
               jailpaywhile = 0
               while jailpaywhile == 0:
                  jailpay = input("Do you want to pay $50 to get out of jail? Type Y or N.")
                  if jailpay == "N":
                     jailpaywhile = 1
                  if jailroll == "Y":
                     player.money += -50
                     player.jailtime = 0
                  else:
                     print("invalid input. Available answers are YES or NO (make sure caps is on).")

            jailrollwhile = 0
            while jailrollwhile == 0:
               jailroll = input("Do you want to try to roll doubles to get out of jail? Type Y or N.")
               if jailroll == "N":
                  jailrollwhile = 1
               if jailroll == "Y":
                  die1 = random.randint(1,6)
                  die2 = random.randint(1,6)
                  print("die 1 roll: " + str(die1))
                  print("die 2 roll: " + str(die2))
                  if die1 == die2:
                     player.jailtime = 0
                     jailrollwhile = 1
                  else:
                     jailrollwhile = 1
               else:
                  print("invalid input. Available answers are YES or NO (make sure caps is on).")
                  


      for colorlist in player.proplist:
         if "monopoly" in colorlist:
            for property in colorlist:
               if property.houses <= 5:
                  housewhile = 0
                  while housewhile == 0:
                     if property.houses == 5:
                        housewhile = 1
                     if player.money >= property.housecost:
                        if player.user == 0:
                           player.money += -property.housecost
                           property.houses += 1
                        if player.user == 1:
                           buyhouseyn = input("Do you want to buy a house on " + property.name + "? Type Y or N.")
                           if buyhouseyn == "N":
                              housewhile = 1
                           if buyhouseyn == "Y":
                              player.money += -property.housecost
                              property.houses += 1
                           else:
                              print("invalid input. Available answers are YES or NO (make sure caps is on).")      
                     else:
                        housewhile = 1


def main():
   print("WELCOME TO MONOPOLY MASTERS' MONOPOLY GAME")
   print(" PLEASE ENTER FOR FUN. " )
   firstwhile = 0
   while firstwhile == 0:
      numplay = int(input("Please enter the number of players you want to play against."))
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
