#Started: November 8 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:

#Description: This is a class that holds all the player's properties and the team's properties since this game is based on teams.
#Variables like score, rounds..etc are stored in this class

#The players have to interact with cards and decks, hence, they're imported.

from Deck import Deck

from Card import Card

class Player :

	def __init__ (self, name) :

		#Each player starts with an empty hand, hence, Deck(False)

		self.name = name

		self.hand = Deck(False)

	def __str__ (self) :

		printer = "\nName: " + self.name + "\nHand:" 

		for i in range(0, len(self.hand.deck)) :

			printer += "\n"

			printer += str(i + 1) + ") " + str(self.hand.deck[i])

		return printer

	#emptyHand is used to clear the hand deck of a player

	def emptyHand (self) :

		self.hand = Deck(False)

	#playCard is an extension of the playCard function in the deck class

	def playCard (self, card) :

		return self.hand.playCard(card)

	#wonRound increments the amount of rounds the player's team won, and self.team refers to the team that the player belongs to

	def wonRound (self) :

		self.team.rounds += 1

	#teamUp links both players to the team class they belong to

	def teamUp (self, other) :

		self.team = Team(self, other)

		other.team = self.team

		return self.team


class Team :

	#Most variables in the team are changed by functions in the player 

	def __init__ (self, player1, player2) :

		self.player1 = player1

		self.player2 = player2

		self.score = 0

		self.challenge = False

		self.rounds = 0

	def __str__ (self) :

		return "Team:\n" + str(self.player1) + "\n" + str(self.player2) + "\n"





