#Started: November 8 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:
#https://stackoverflow.com/questions/27694357/python-cannot-import-name
#http://letzgro.net/blog/creating-ai-using-python/

#Description: This is a class that holds all the player's properties and the team's properties since this game is based on teams.
#This class also holds the playing strategy and functions for computer players
#Variables like score, rounds..etc are stored in this class

#The players have to interact with cards and decks, hence, they're imported.

from Deck import Deck

from Card import Card

suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

class Player :

	#The comm boolean distinguishes between computer and non computer players, and it's false by default.

	def __init__ (self, name, comm = False) :

		#Each player starts with an empty hand, hence, Deck(False)

		self.comm = comm

		#If it is declared true, the player creates a comm to control it (self.com)

		if self.comm == True :

			self.com = Comm(self)

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

suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

#Comm class contains the functions for an automatic computer player

class Comm :

	#The player variable gives the comm access to the player its controlling

	def __init__(self, player) :

		self.player = player

	#playCard() is for a comm player that starts the round, so it can't start with the joker, so it checks if the first card is a joker.
	#If it isn't, it returns its position, otherwise, it returns the next card's position

	def playCard(self) :

		if self.player.hand.deck[0].suite != "Joker" :

			return 0

		else :

			return 1

	#declare() is the automatic declaration function for a comm player, it never goes above five, and picks the suite that it has most of

	def declare(self) :

		global suites

		lis = [0, 0, 0, 0]

		for i in range(0, len(self.player.hand.deck)) :

			if self.player.hand.deck[i].suite == "Diamonds" :

				lis[0] += 1

			elif self.player.hand.deck[i].suite == "Hearts" :

				lis[1] += 1

			elif self.player.hand.deck[i].suite == "Spades" :

				lis[2] += 1

			elif self.player.hand.deck[i].suite == "Clovers" :

				lis[3] += 1

		high = 0

		for i in range(0, len(lis)) :

			if lis[i] > high :

				high = lis[i]

		return [5, high]

	#commPlay() is a function for a comm player that isn't starting the round, so it has to abide by the round's suite
	#It's programmed to play the Joker ASAP so that it doesn't stay till the end when it can't be played

	def commPlay(self, roundSuite) :

		i = 0

		while i < len(self.player.hand.deck) :

			if self.player.hand.deck[i].suite == "Joker" :

				return self.player.playCard(i)

			i += 1

		i = 0

		while i < len(self.player.hand.deck) :

			if self.player.hand.deck[i].suite == roundSuite :

				return self.player.playCard(i)

			i += 1

		return self.player.playCard(0)







