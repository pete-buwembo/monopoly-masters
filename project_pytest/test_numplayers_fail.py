import pytest

# Monopoly is set to have 2 to 4 players
# Designate fixture to return list of 3 values (2, 3, 4) for number of players
# If the number is not in the list, then number of players allowed is not triggered, so fail
# If the number is in the list of number of players, then number of players allowed is triggered, so pass

@pytest.fixture

def numplayers_A_B_C(): 
	a=2
	b=3
	c=4
	return [a,b,c]

# When z = 5, tests should fail
def test_comparewithA(numplayers_A_B_C):
	z=5
	assert numplayers_A_B_C[0]==z,"a and z comparison failed"

def test_comparewithB(numplayers_A_B_C):
	z=5
	assert numplayers_A_B_C[1]==z,"b and z comparison failed"

def test_comparewithC(numplayers_A_B_C):
	z=5
	assert numplayers_A_B_C[2]==z,"c and z comparison failed"
