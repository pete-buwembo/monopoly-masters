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

# When set z as one of the card space numbers, the test at that space should pass 
def test_comparewithA(cards_A_B_C):
	z=7
	assert cards_A_B_C[0]==z,"a and z comparison failed"

def test_comparewithB(cards_A_B_C):
	z=22
	assert cards_A_B_C[1]==z,"b and z comparison failed"

def test_comparewithC(cards_A_B_C):
	z=36
	assert cards_A_B_C[2]==z,"c and z comparison failed"