import pytest

class DiceRoll(): 
        # initialize the class
    def __init__(self, d= 0): 
        self.d = d
    
    def dicenum(self, rollnum):
        if rollnum < 0:
            print("die number greater than 1")
        self.d = self.d + rollnum
        
class LetsRoll(DiceRoll): 
    def dicenum(self, rollnum):
        if rollnum > self.d:
            print ("Dice roll valid")

def test_roll1():
    a = LetsRoll(1)
    a.dicenum(1)
    assert a.d == 1

def test_roll2():
    b = LetsRoll(1)
    b.dicenum(6)
    assert b.d == 6


