#Started: November 1 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:


#Description: This is a class that holds all the card's properties including suites, ranks, and print value

#outOfBoundsError is an error that appears whenever you try to declare a card with an invalid value for rank or number
class outOfBoundsError (Exception) :

	pass


class Card :

	def __init__ (self, suite = "Joker", number = 0) :

		#Suite is declared by numbers to make it easier to craete a deck, that maps to a value in the (suites) list later on

		suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

		#Flipped gives a variable to differentiate face-down cards from face-up cards, in case it was to be used to conceal face-down cards

		self.flipped = False

		self.number = number

		if number != 0 :

			self.suite = suites[suite - 1]

			if suite > 4 :

				raise outOfBoundsError("Value out of bounds.")


		else :

			self.suite = suite

			#Same with the suite, the rank maps to a certain entity in the numbers list, and that is based on the number variable declared with the card
		
		numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

		self.number = number

		self.rank = numbers[number - 1]

		if number > 13 or number < 0 :

			raise outOfBoundsError("Value out of bounds.")

	def __str__ (self) :

		#If a card is flipped, it returns a "Flipped Card" string, otherwise it prints the card is the format: (Suite of Rank), and if it's a Joker, it simply prints "Joker"

		if self.flipped == False :

			if self.suite != "Joker" :

				return str(self.rank) + " of " + self.suite

			else :

				return "Joker"

		else :

			return "Flipped Card"







