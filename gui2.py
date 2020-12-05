import random
import math
import sys

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