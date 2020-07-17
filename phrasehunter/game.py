import random

from phrasehunter.phrase import Phrase


class Game:
	def __init__(self, phrases):
		self.phrases = [Phrase(phrase) for phrase in phrases]
		self.lives = 5
		self.guessed_letters = []

		print(f"""{"*" * 10}Welcome to PHRASE HUNTER!{"*" * 10}""")


	def start_game(self):
		self.active_phrase = random.choice(self.phrases)
		print("\nGuess the phrase!")
		self.active_phrase.show_display()
		
		attempt = 0
		while attempt < self.lives:
			if self.player_guess():
				print("\n")
			else:
				attempt+=1
				print("\nOops! You have {} out of {} lives remaining!\n".format(self.lives - attempt, self.lives))
			
			self.active_phrase.show_display()

			if self.active_phrase.is_guessed():
				self.game_result(win=True)
				break
		else:
			self.game_result(win=False)


	def player_guess(self):
		user_guess = self.validate_guess()
		self.guessed_letters.append(user_guess)

		if self.active_phrase.check_guess(user_guess):
			return True
		else:
			return False


	def validate_guess(self):
		while True:
			try:
				user_guess = input("\nGuess a letter: ")
				if len(user_guess) != 1 or user_guess.isalpha() == False:
					raise ValueError("Invalid guess. Please only guess ONE LETTER at a time.")
				elif user_guess in self.guessed_letters:
					raise ValueError("You have already guessed that letter. Guess a new letter.")
			except ValueError as err:
				print("{}".format(err))
			else:
				break
		return user_guess


	def game_result(self, win=False):
		print("\n")
		if win:
			print("Congratulations! You've guessed it right! ^.^")
		else:
			print("Game Over.\nYou ran out chances!")
