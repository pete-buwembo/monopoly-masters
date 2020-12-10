import datetime


class BankAccount():
        # initializing the class
	def __init__(self, name = 'Timbler', ID = '1', creation_date = datetime.date.today(), balance = 1500):
		self.name = name
		self.ID = ID
		self.creation_date = creation_date
		self.balance = balance

	# this function takes the amount you put in as desposit
	def deposit(self, amount):
		if amount < 0:
			print("Negative deposit not allowed. Request to withdraw instead")
                # Balance was zero but when you deposit it increases by the amount of deposit
		self.balance = self.balance + amount

	def withdraw(self, amount):
		self.balance = self.balance - amount

	def view_balance():
		print("The balance on the account is" + self.balance)

class SavingsAccount(BankAccount):
	def withdraw(self, amount):
		if amount > self.balance:
			print("Overdrawing the account is not permitted")
		elif (datetime.date.today() - self.creation_date).days < 180:
			print("less than 180 days since account opening")
		else: self.balance = self.balance - amount

def test_constructor():
	a = BankAccount()
	#assert a.creation_date == datetime.date(2020, 12,9)
	assert a.creation_date == datetime.date.today()

def test_savings_deposit():
	b = SavingsAccount('Boot', '2', datetime.date(2020, 12, 9), 1500)
	b.deposit(200) # Boot cross start line and gets $200
	assert b.balance == 1700

def test_savings_withdraw():
	c = SavingsAccount('Boot', '2', datetime.date(2019, 12, 9), 1700)
	c.withdraw(100) # Boot lands on property and decides to purchase it at $100 so minus $100 from the account
	assert c.balance == 1600

def test_savings_negative():
	c = SavingsAccount('Boot', '2', datetime.date(2020, 12, 9), 1700)
	c.withdraw(1800) # Boot lands on friend's property and has to pay more than he has in bank so can't pay
	assert c.balance == 1700

