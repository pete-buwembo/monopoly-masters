import pytest

# Monopoly is set to have 2 to 4 players
# Designate fixture to return list of 3 values (2, 3, 4) for number of players
# If the number is not in the list, then number of players allowed is not triggered, so fail
# If the number is in the list of number of players, then number of players allowed is triggered, so pass

@pytest.fixture

def cards_A_B_C(): 
	a=2
	b=3
	c=4
	return [a,b,c]

# When set z as one of the card space numbers, the test at that space should pass 
def test_comparewithA(cards_A_B_C):
	z=2
	assert cardss_A_B_C[0]==z,"a and z comparison passed"

def test_comparewithB(cards_A_B_C):
	z=3
	assert cards_A_B_C[1]==z,"b and z comparison passed"

def test_comparewithC(cards_A_B_C):
	z=4
	assert cards_A_B_C[2]==z,"c and z comparison passed"