def draw(self):
    # Draw the current card
    card = self.cards[self.nextCard]

    # Step to the next place in the list, wrapping around if necessary.
    self.nextCard = self.nextCard + 1
    if self.nextCard >= self.ncards:
        self.nextCard = 0

    # Return the card
    return card

    # Build the card decks
    def createCardDecks(self):

        # Create two lists to hold possible results from picking a card
        chanceResults = []
        communityChestResults = []

        # These are all commands to go to a square
        chanceResults += [ (0, 1) ] # Advance to GO (PLACEHOLDER)
        chanceResults += [ (0, 2) ] # Advance to Pall Mall (PLACEHOLDER)
        chanceResults += [ (0, 3) ] # Go to Jail (PLACEHOLDER)
        chanceResults += [ (0, 3) ] # Take a trip to Marylebone Station (PLACEHOLDER)
        chanceResults += [ (0, 4) ] # Advance to Mayfair (PLACEHOLDER)
        chanceResults += [ (0, 5) ] # Advance to Trafalgar square (PLACEHOLDER)

        # This is an offset
        chanceResults += [ (1, -3) ] # Go back three spaces (PLACEHOLDER)

        # Now create the deck of cards
        self.chanceDeck = Deck(16, chanceResults) # There are sixteen cards in the deck. (PLACEHOLDER)
        self.chanceDeck.shuffle() # Call this once at the start of the game. (PLACEHOLDER)

        # These are all commands to go to a square
        communityChestResults += [ (0, 1) ] # Advance to GO (PLACEHOLDER)
        communityChestResults += [ (0, 2) ] # Go to Jail (PLACEHOLDER)
        communityChestResults += [ (2, 0) ] # Pay 10 pounds or take a chance (PLACEHOLDER)

        # Now create the deck of cards
        self.communityChestDeck = Deck(16, communityChestResults) # There are sixteen cards in the deck.
        self.communityChestDeck.shuffle() # Call this once at the start of the game.