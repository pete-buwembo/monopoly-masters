import pytest

# When stop on space 2, 17 and 33 on the board, chance cards are triggered
# Designate fixture to return list of 3 values (2, 17, and 33) on the board
# If the space landed is not in the list, then cards are not triggered, so fail
# If the space landed is in the list, then cards are triggered, so pass

@pytest.fixture

def cards_A_B_C(): 
	a=2
	b=17
	c=33
	return [a,b,c]

# When z = 35, tests should fail because not 2, 17, 33
@pytest.mark.xfail
def test_comparewithA(cards_A_B_C):
	z=35
	assert cards_A_B_C[0]==z,"a and z comparison failed"
@pytest.mark.xfail
def test_comparewithB(cards_A_B_C):
	z=35
	assert cards_A_B_C[1]==z,"b and z comparison failed"
@pytest.mark.xfail
def test_comparewithC(cards_A_B_C):
	z=35
	assert cards_A_B_C[2]==z,"c and z comparison failed"