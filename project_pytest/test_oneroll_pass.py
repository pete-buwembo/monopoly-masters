import pytest

# One die has 6 faces, number 1 to 6
# To make sure that the randomizer is set up to roll between 1 to 6
# designate fixture to return list of 6 values (1, 2, 3, 4, 5, 6) for one die
# If the roll is not in the list, then fail
# If the roll is on the list, then pass

@pytest.fixture

def roll_A_B_C_D_E_F(): 
	a = 1
	b = 2
	c = 3
	d = 4
	e = 5
	f = 6
	return [a, b, c, d, e, f]

# When z = 1, 2, 3, 4, 5 or 6 at appropriate face, tests should pass
def test_comparewithA(roll_A_B_C_D_E_F):
	z=1
	assert roll_A_B_C_D_E_F[0]==z,"a and z comparison passed"

def test_comparewithB(roll_A_B_C_D_E_F):
	z=2
	assert roll_A_B_C_D_E_F[1]==z,"b and z comparison passed"

def test_comparewithC(roll_A_B_C_D_E_F):
	z=3
	assert roll_A_B_C_D_E_F[2]==z,"c and z comparison passed"

def test_comparewithD(roll_A_B_C_D_E_F):
	z=4
	assert roll_A_B_C_D_E_F[3]==z,"d and z comparison passed"

def test_comparewithE(roll_A_B_C_D_E_F):
	z=5
	assert roll_A_B_C_D_E_F[4]==z,"e and z comparison passed"

def test_comparewithF(roll_A_B_C_D_E_F):
	z=6
	assert roll_A_B_C_D_E_F[5]==z,"f and z comparison passed"

