# The number of squares on the board
nsquares = 40

# A variable to hold the current position
currentPosition = 0

class MonopolySimulation:
    def __init__(self):

        # The position of the chance and community chest squares
        self.chance = [7, 22, 36]
        self.communityChest = [2, 17, 33]

        self.chanceDeck = None
        self.communityChestDeck = None
        self.createCardDecks()

        # The number of squares on the board
        self.nsquares = 40

        # A list to contain the total value rolled.
        self.counters=[0.]*self.nsquares

        # A variable to hold the current position
        self.currentPosition = 0

    #-----------------------------------------------

    # Build the card decks
    def createCardDecks(self):

        # Create two lists to hold possible results from picking a card
        chanceResults = []
        communityChestResults = []

        # These are all commands to go to a square
        chanceResults += [ (150, 0) ] # Advance to GO
        chanceResults += [ (0, 11) ] # Advance to Pall Mall
        chanceResults += [ (0, 10) ] # Go to Jail
        chanceResults += [ (80, 0) ] # Win lottery and get 80 pounds
        chanceResults += [ (0, 39) ] # Advance to Mayfair
        chanceResults += [ (0, 24) ] # Advance to Trafalgar square

        # This is an offset
        chanceResults += [ (1, -3) ] # Go back three spaces

        # Now create the deck of cards
        self.chanceDeck = Deck(16, chanceResults) # There are sixteen cards in the deck.
        self.chanceDeck.shuffle() # Call this once at the start of the game.

        # These are all commands to go to a square
        communityChestResults += [ (0, 0) ] # Advance to GO
        communityChestResults += [ (0, 10) ] # Go to Jail
        communityChestResults += [ (2, 0) ] # Pay 10 pounds or take a chance

        # Now create the deck of cards
        self.communityChestDeck = Deck(16, communityChestResults) # There are sixteen cards in the deck.
        self.communityChestDeck.shuffle() # Call this once at the start of the game.
