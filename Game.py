#Started: November 8 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:
#https://stackoverflow.com/questions/12614334/typeerror-bool-object-is-not-callable
#https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
#http://letzgro.net/blog/creating-ai-using-python/


#Description: This program implements a card game called Kout. The game has 4 players, each 2 facing each other are a team. The deck consists of 32 cards
#which are all the cards higher than 7 plus the ace. The 7 of Diamonds is taken off to make place for the Joker. Each player gets 8 cards out of the shuffled deck.
#In the beginning of each game in the game, at least one player has to declare how many rounds they're going to take on this particular round. If no one declares,
#the cards are shuffled and re-distributed. Each game has 8 rounds, and in each round, all players play one card. The strongest card wins the round, 
#and the winning player starts the next round. In the declaration phase, the player has to either pass, or declare how many rounds they're going to take.
#That number can't be more than 8, as there are only 8 rounds, and it can't be less than five, as that would be a 50-50 split If the player fulfills the declaration, 
#they win, otherwise, they lose. If a player declares, other players are allowed to increase over his/her declaration, but not declare the same.
#The declaring player also declares a dominant suite. The dominant suite are the strongest cards aside from the Joker. 
#The order of strength goes: Ace, King, Queen, Jack, 10, 9, 8, 7. The player to the right of the declaring player starts the round, giving him the 
#power to decide the round's suite. Whichever suite he/she plays is the round's suite. You can't play a card from another suite if you have a card from the round's suite. 
#If you don't, however, cards which are from the dominant suite and the Joker are the strongest, and other suites (excluding the round's suite) are useless. The scoring 
#system works like a scale; if your team loses a game, the scale is tipped against you, and if you win, it's tipped the other way. For example, say you win a declaration
#of 5, that's 5 points for your team, or 5 points against the other team. If you lose your declaration, however, you get twice the declaration amount against you, for 
#instance, if you declared 6 and lost, you get 12 points against you. Declaration of 8 is the exception; if you win, you win the whole game, if you lose, you lose everything
#The games continue until the score reaches 32, at which point, the team with 32 points for them wins

#Card class 
from Card import Card
#Deck class
from Deck import Deck
#Player, team, and computer player classes
from Player import Player
from Player import Team
from Player import Comm
#Filters a 52 card deck into a Kout deck
def Filter (Deck) :

	filtered = []

	for i in range(0, len(Deck.deck)) :
#The Ace (1) and all cards 7 through K are appended into a list and returned
		if int(Deck.deck[i].number) >= 7 or int(Deck.deck[i].number) < 2 :

			filtered.append(Deck.deck[i])

	del filtered[1]

	return filtered
#Deals 8 cards to each of the 4 players
def Deal (deck, players) :

	for i in range (0, 4) :

		for j in range (0, 8) :

			players[i].hand.drawCard(deck)

#The main deck from which all cards are dealt
mainDeck = Deck()

mainDeck.deck = Filter(mainDeck)
#HK is a variable to hold the dominant suite
HK = ""
#The suites list is used to map the initial HK value to an actual suite
suites = ["Diamonds", "Hearts", "Spades", "Clovers"]
#Initialize starts out the game, contains the declaration phase, returns a list with the declaring player and his declaration value
def initialize (players) :

	global mainDeck

	global HK

	global suites

	#The lastPlayer variable holds the position of the declaring player in the (players) list. the initial value is 5 because that value is out of index, 
	#and if no one declatres, that value remains at 5 prompting a loop-back

	lastPlayer = 5

	while lastPlayer == 5 :

		#The deck is refreshed everytime the loop starts, so that if no one declares, the cards are re-shuffled

		mainDeck = Deck()

		mainDeck.deck = Filter(mainDeck)

		for i in range(0, len(players)) :

			#All players' hands are emptied before dealing just in case theres something there

			players[i].emptyHand()

		print("\n")

		mainDeck.shuffle()

		Deal(mainDeck, players)

		high = 0

		#Declaration phase starts

		for i in range(0, 4) :

			if players[i].comm == False :

				print(players[i])

				answer = input("Do you want to challenge?\n")

				if str(answer).lower() == "yes" or str(answer).lower() == "y" :

					#bet is the variable that holds the declaration value, high holds the highest declaration value thus far

					bet = 0

					while (bet < 5 or bet > 8) :

						#xcr and xer are check booleans to loop back for error in input value

						xer = True

						xcr = True

						while xer == True or xcr == True :

							bet = input("How Much? \n")

							if str(bet).isnumeric() == True :	

								bet = int(bet)

								xer = False

								if bet > 4 and bet > high and bet < 9 :

									high = bet 

									lastPlayer = i

									xcr = False

									#xbr is a check boolean to loop back for error in input value

									xbr = True

									while xbr == True :

										HK = input("Choose your suite:\n1) Diamonds\n2) Hearts\n3) Spades\n4) Clovers\n")

										if HK.isnumeric() == True :

											if int(HK) >= 1 and int(HK) <= 4 :

												HK = int(HK)

												HK = suites[HK - 1]

												xbr = False

											else :

												print("Invalid input\nTry again.\n\n")

										else: 

											print("Invalid input\nTry again.\n\n")

								else :

									print("Invalid input\nTry again.\n\n")

							else:

								print("\nInvalid input\nTry Again.\n\n")

			#If the player is a computer player, it resorts to the declare function in the Comm class

			else :

				if high < 5 :

					lastPlayer = i

					high = players[i].com.declare()[0]

					HK = players[i].com.declare()[1]

					HK = suites[HK - 1]

			#8 is the highest value, so if a player declares 8, no one can one-up that so the loop breaks

			if high == 8 :

				return [lastPlayer, high]

				break

	#return the postion of the last player and his declaration value

	return [lastPlayer, high]

#teamUp id a fuction for connecting the players and the teams

def teamUp (player1, player2) :

	return player1.teamUp(player2)

#suiteCheck checks if you're violating the round's suite

def suiteCheck (player, suite) :

	for i in range(0, len(player.hand.deck)) :

		if player.hand.deck[i].suite == suite :

			return True

	return False

#roundCheck checks for the strongest card in a round, pile is the list of cards played in that round

def roundCheck (roundSuite, HK, pile) :

	highnum = 0

	piled = pile

	for i in range(0, len(piled)) :

		#Joker is the strongest card so if a card is the joker, that makes it the winner regardless, hence, if the card's a joker the function is over

		if piled[i].suite == "Joker" :

			return i

		#If a card is the dominant suite, it wins over the round's suite

		elif piled[i].suite == HK :

			high = i

			highnum = piled[i].number

			#If a card is dominant suite, we have to check for the joker because it's the only suite higher than the dominant suite.

			for j in range(i, len(piled)) :

				if piled[j].suite == "Joker" :

					return j

				#Since an Ace's number is 1, theres an exception for it for the program to detect it as stronger than K, Q ,J...etc

				elif piled[j].suite ==	HK and piled[j].rank == "Ace" :

					for k in range(j, len(piled)) :

						#The only thing higher than an ace in the dominant suite is the Joker

						if piled[k].suite == "Joker" :

							return k

					return j

				#If it isn't the ace or a joker, it cycles through the rest checking if theres a higher number

				elif piled[j].suite ==	HK and piled[j].number > highnum :

					high = j 

					highnum = piled[j].number

			return high

		else :

			#If it isn't joker or dominant suite, it checks for the rest, the round's suite

			if piled[i].suite == roundSuite and piled[i].rank == "Ace" :

				for j in range(i, len(piled)) :

					if piled[j].suite == "Joker" :

						return j

				return i

			elif piled[i].suite == roundSuite and piled[i].number > highnum :

				high = i

				highnum = piled[i].number

	return high

#checkWin returns the amount of points for the challenging team, the other team gets the negative of that, since it's a scale system

def checkWin (bet, rounds) :

	if rounds < bet :

		return (-2 * bet)

	else :

		return bet

#rounds is the function that actually runs the game, or the rounds, and returns the amount of points for the declaring team


def rounds (players, stage, bet, challenger) :

	global HK

	#This function recurrs 8 times, so the stage variable increments every time so that the function ends after that

	if stage < 8 :

		print("Declarer: " + players[0].name)

		print("Amount: " + str(bet) + " Rounds")

		print("\n\nDominant Suite: " + HK)

		pile = []

		if players[0].comm == False :

			print(players[0])

			#Players can't start with the joker, so if they don't have another card to play, the other team automatically wins

			if stage == 7 and players[0].hand.deck[0].suite == "Joker" :

				print("Oops!\nLooks like you held on to that joker a little too long.")

				if players[0].team == challenger.team :

					return checkWin(bet, 0)

				else :

					return checkWin(bet, 8)

			#xer is a check boolean to loop back in case of input errors

			xer = True

			#This part is only for the player starting the round

			while xer == True :

				card = input("Play a card:\n")

				if card.isnumeric() == True :

					card = int(card)

					if card > 0 and card <= len(players[0].hand.deck) :

						card = int(card) - 1

						if players[0].hand.deck[card].suite != "Joker" :
			
							xer = False

						#Players can't start with the joker

						else:

							print("\nYou can't start with the joker\nTry Again.\n\n")

					else :

						print("\nInvalid input\nTry Again.\n\n")

				else:

					print("\nInvalid input\nTry Again.\n\n")
		#If the player's a computer, it resorts to the playCard function in the Comm class

		else :

			card = players[0].com.playCard()

		#roundSuite stores the round's suite

		roundSuite = players[0].hand.deck[card].suite

		#pile holds the round's cards

		pile.append(players[0].hand.playCard(card))

		#this part is for the players other than the first player in the round

		for i in range(1, len(players)) :

			if players[i].comm == False : 

				print("\nCurrent pile:")

				for j in range(0, len(pile)) :

					print(str(pile[j]))

				print("\n\nDominant Suite: " + HK)

				print("Round Suite: " + roundSuite)

				print(players[i])

				xer = True

				while xer == True :

					card = input("Play a card:\n")

					if card.isnumeric() == True :

						card = int(card)

						if card > 0 and card <= len(players[i].hand.deck) :

							card = int(card) - 1

							#Checks if the player has the round's suite, and if they do, it doesn't allow them to play another suite aside from the Joker

							if suiteCheck(players[i], roundSuite) == True and players[i].hand.deck[card].suite != roundSuite and players[i].hand.deck[card].suite != "Joker" :

								print("Suite invalid.\nTry Again.\n\n")

							else :

								pile.append(players[i].hand.playCard(card))

								xer = False

						else :

							print("\nInvalid input\nTry Again.\n\n")

					else:

						print("\nInvalid input\nTry Again.\n\n")

			#If the player's a computer, it resorts to the commPlay method in the Comm class
			
			else :

				pile.append(players[i].com.commPlay(roundSuite))

		print("\nCurrent pile:")

		for j in range(0, len(pile)) :

			print(str(pile[j]))

		print("\n")

		#Returns the position of the winning player in the (players) list

		winner = roundCheck(roundSuite, HK, pile)

		stage += 1

		players[winner].wonRound()

		#prints the amount of rounds each player has won

		print("\n\nTeam 1: " + str(player1.team.rounds) + " Round(s)")

		print("Team 2: " + str(player2.team.rounds) + " Round(s)\n\n")

		#Next round starts with the player who won the previous round

		rounds([players[winner], players[(winner + 1) % 4], players[(winner + 2) % 4], players[(winner + 3) % 4]], stage, bet, challenger)

	return checkWin(bet, challenger.team.rounds)

#Pre-Initialization, setting player names, to initialize a comm player, you have to start the name with "comm" no case sensitivity

print("\n\n\nWelcome to Kout :)\n\nTo add a computer layer, start the player name with 'comm.'\nExample: Player 1 Name: commBasic\n\n\n")

scanner = str(input ("Player 1 Name: "))

if scanner.lower().startswith("comm") == True :

	player1 = Player(scanner, True)

else: 

	player1 = Player(scanner)

scanner = str(input ("Player 2 Name: "))

if scanner.lower().startswith("comm") == True :

	player2 = Player(scanner, True)

else: 

	player2 = Player(scanner)

scanner = str(input ("Player 3 Name: "))

if scanner.lower().startswith("comm") == True :

	player3 = Player(scanner, True)

else: 

	player3 = Player(scanner)

scanner = str(input ("Player 4 Name: "))

if scanner.lower().startswith("comm") == True :

	player4 = Player(scanner, True)

else: 

	player4 = Player(scanner)

#Players facing each other are in the same team, hence, 1 and 3 are the same team, same goes for 2 and 4

team1 = teamUp(player1, player3)

team2 = teamUp(player2, player4)

lis = [team1.player1, team2.player1, team1.player2, team2.player2]

teams = [team1, team2]

#The games continue until the score is 32

while abs(team1.score) < 32 or abs(team2.score) < 32 :

	#Each game, the rounds are reset for the next one

	team1.rounds = 0

	team2.rounds = 0

	#param stores the highest declaration value and the declaring player position

	param = initialize(lis)

	lastPlayer = lis[param[0]]

	score = rounds ([lis[(param[0] + 1) % 4], lis[(param[0] + 2) % 4], lis[(param[0] + 3) % 4], lis[(param[0] + 4) % 4]], 0, param[1], lastPlayer)

	if abs(score) == 16 :

		score = 2 * score

	#The non-declaring team gets the negative amount of poin

	lastPlayer.team.score += score

	lis[(param[0] + 1) % 4].team.score -= score

	#At the end of each game, the scores are displayed

	print("Team 1: " + str(team1.score) + " points")

	print("Team 2: " + str(team2.score) + " points")

for i in range(0, 2) :

	#Ends the game by declaring the winner

	if teams[i].score > 0 :

		if teams[i] == team1 :

			print("\n\nTeam 1 Wins!")

		else: 

			print("\n\nTeam 2 Wins!")

#The End!

#Thank you.
