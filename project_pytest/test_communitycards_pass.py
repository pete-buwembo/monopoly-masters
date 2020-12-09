import pytest

# When stop on space 2, 17 and 33 on the board, community chest cards are triggered
# Designate fixture to return list of 3 values (2, 17 and 33) on the board
# If the space landed is not in the list, then cards are not triggered, so fail
# If the space landed is in the list, then cards are triggered, so pass

@pytest.fixture

def cards_A_B_C(): 
	a=2
	b=17
	c=33
	return [a,b,c]

# When set z as one of the card space numbers, the test at that space should pass 
def test_comparewithA(cards_A_B_C):
	z=2
	assert cards_A_B_C[0]==z,"a and z comparison passed"

def test_comparewithB(cards_A_B_C):
	z=17
	assert cards_A_B_C[1]==z,"b and z comparison passed"

def test_comparewithC(cards_A_B_C):
	z=33
	assert cards_A_B_C[2]==z,"c and z comparison passed"