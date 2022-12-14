# THERE ARE NO ACES

# Imports
import sys, os, random, time
from colorama import Fore, Style

# Vars
rand_num = random.randint(0, 100)
# ace, #, queen, king
deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
global playerWallet
playerWallet = 0
dealerCards = []
playerCards = []

# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def draw():
	chosenCard = random.choice(deck_of_cards)
	return chosenCard
def table_setup():
	dealerCards.append(draw())
	dealerCards.append(draw())
	playerCards.append(draw())
	playerCards.append(draw())

# Starting cash
def start_cash():
	startingCash = input('How much money would you like to start with? ')
	if int(startingCash) > 0:
		playerWallet = int(startingCash)
		print(playerWallet)
	else:
		print('Value must be an integer')
		time.sleep(2)
		quit()

# Main
def main_game():
	# Needed functions
	def hit_or_stand():
		hitORstand = input('(H)hit or (S)stand: ')
		if hitORstand.lower() == 'h':
			playerCards.append(draw())
			print('_-Hit-_')
			print('Players Cards:', playerCards)
			print('Dealers Cards:', dealerCards)
			check_cards()
			print('-------------------')
		if hitORstand.lower() == 's':
			print()
			if sum(dealerCards) > sum(playerCards):
				print(Fore.RED+'Dealer Wins')
				print('Players Cards:', playerCards)
				print('Dealers Cards:', dealerCards, Style.RESET_ALL)
				print('-------------------')
			if sum(dealerCards) < sum(playerCards):
				print(Fore.GREEN+'Player Wins')
				global playerWallet
				newWallet = (int(playerBet) * 2) + playerWallet
				playerWallet = newWallet
				print('Players Cards:', playerCards)
				print('Dealers Cards:', dealerCards, Style.RESET_ALL)
				print('-------------------')
			else:
				print('Invaild input')
				time.sleep(3)
				main_game()
		else:
			print(Fore.RED+'Invalid input'+Style.RESET_ALL)
			time.sleep(2)
			quit()
		time.sleep(3)
		main_game()

	def check_cards():
		if sum(dealerCards) > 21:
			print(Fore.GREEN+'Dealer Bust'+Style.RESET_ALL)
			playerWallet + int(playerBet) * 2
			time.sleep(1)
			main_game()
		if sum(playerCards) > 21:
			print(Fore.RED+'Player Bust'+Style.RESET_ALL)
			sum(playerCards) - int(playerBet)
		if sum(playerCards) == 21:
			print('Player Blackjack')
		if sum(dealerCards) == 21:
			print('Dealer Blackjack')

	# Main
	start_cash()
	table_setup()
	print('Money: ', playerWallet, '\n')
	print('Your Cards', '          ', 'Dealer Cards')
	one_dealerCard = [dealerCards[1]]
	print(playerCards, '              ', one_dealerCard)
	# Start betting phase
	playerBet = input('\nYour Bet: ')
	if playerWallet < int(playerBet):
		print('Your bet is to high...')
		time.sleep(2)
		CC()
		main_game()
	else:
		playerWallet - int(playerBet)
		print('-------------------')
		time.sleep(1)

	# Start Hit or Stand
	hit_or_stand()

# Call to
if __name__ == '__main__':
	print('SCRIPT MODE: ON')
	time.sleep(2)
	CC()
	main_game()
else:
	main_game()

