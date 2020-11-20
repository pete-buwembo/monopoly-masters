import pytest

# When stop on space 7, 22 and 36 on the board, chance or community cards 
# are triggered
# Designate fixture to return list of 3 values (7, 22 and 36) on the board
# If the space landed is not in the list, then cards are not triggered
# If the space landed is in the list, then cards are triggered

@pytest.fixture

def cards_A_B_C(): 
	a=7
	b=22
	c=36
	return [a,b,c]

# When z = 35, tests should fail because not 7, 22 or 36
def test_comparewithA(cards_A_B_C):
	z=35
	assert cards_A_B_C[0]==z,"a and z comparison failed"

def test_comparewithB(cards_A_B_C):
	z=35
	assert cards_A_B_C[1]==z,"b and z comparison failed"

def test_comparewithC(cards_A_B_C):
	z=35
	assert cards_A_B_C[2]==z,"c and z comparison failed"