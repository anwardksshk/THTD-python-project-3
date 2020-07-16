import random

from phrasehunter.phrase import Phrase


# Create your Game class logic in here.
class Game(Phrase):
	def __init__(self, phrase=None, lives=5):
		self.phrase = phrase
		self.lives = lives
		self.active_phrase = self.phrase[random.randint(0,len(self.phrase))]
		super().__init__(self.active_phrase)
		print(f"""{"*" * 10}Welcome to PHRASE HUNTER!{"*" * 10}""")
		print("{}".format(self.active_phrase))


	#game loop
	def start_game(self):
		print("Guess the phrase!")
		super().show_letters()

		attempt = 0
		while attempt < self.lives:
			if self.player_guess():
				pass
			else:
				attempt+=1
				print("\nYou have {} out of {} lives remaining!\n".format(self.lives - attempt, self.lives))

			if super().is_guessed():
				self.lives -= attempt
				self.game_result()
				break	

		else:
			print("Game Over!!!!")
			


	#player input/guess
	def player_guess(self):
		guess_letter = input("\nGuess a letter: ")
		if super().check_guess(guess_letter):
			return True
		else:
			return False
				

	#determine win_lose	
	def game_result(self):
		print(f"""{"*" * 30}""")
		print("You win with {} lives left! Congratulations!".format(self.lives))
