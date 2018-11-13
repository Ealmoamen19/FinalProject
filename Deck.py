#Started: November 6 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:

#Description: This is a class that holds all the deck's properties and functions including it's cards, drawing cards, printing a specific card, shuffling the deck..etc 

#The deck class is based on the card class, hence, it's imported.
from Card import Card

import random

class Deck :

	def __init__ (self, stats = True) :

		#self.deck is a list that stores all the deck's cards

		self.deck = []

		#self.main decides if this is a main deck or a hand. If it's a main deck, all 52 cards plus the Joker will be appended to self.deck

		self.main = stats

		if self.main == True :

			for i in range(1, 5) :
				for j in range(1, 14):

					self.deck.append(Card(i, j))

			self.deck.append(Card())

		#self.printer is used later on as a string that contains all the cards in the deck separated by line breaks

		self.printer = ""

	#addCard is to add a certain card to a deck or a hand

	def addCard (self, appendee) :

		self.deck.append(appendee)

	#printCard to print a specific card out of the deck

	def printCard (self, position) :

		return self.deck[position]

	def __str__ (self) :

		#All cards are appended to a string separated by line breaks

		for i in range(0, len(self.deck)) :

			self.printer = self.printer + "\n" + str(self.deck[i])

		return self.printer

	#shuffle is a method to shuffle the deck. It does so by picking a random card from self.deck, and appending it to another list(shuffled), it does that until all the cards 
	#that were in the main deck are in the new deck, and then sets self.deck to the new deck

	def shuffle (self) :

		deck = self.deck

		shuffled = []

		for i in range(0, len(self.deck)) :

			x = random.choice(deck)

			shuffled.append(x)

			deck.remove(x)

		self.deck = shuffled

	#drawCard has two parameters; the deck of cards you're drawing from (other), and your deck, so it removes the last card from the other deck and then appends it to 
	#self.deck

	def drawCard (self, other) :

		card = other.deck[len(other.deck) - 1]

		del other.deck[len(other.deck) - 1]

		self.deck.append(card)

	#playCard removes whatever card you pick from the deck and returns the value

	def playCard(self, card) :

		store = self.deck[card]
		
		del self.deck[card]

		return store
