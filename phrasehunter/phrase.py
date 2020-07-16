from phrasehunter.character import Character

# Create your Phrase class logic here.
class Phrase(Character):
	# winning_points = 0

	def __init__(self, phrase=None):
		self.phrase = phrase #phrase in string
		self.phrase_letters = [char for char in self.phrase] #a List of each char in string
		self.guess_letter =[] #list of all guessed letters including the wrong ones
		self.display = [] #The display
		# super().__init__(self.phrase_letters)
		super().__init__([char for char in self.phrase])


	#knowing the entire phrase has been guessed or not
	def is_guessed(self):
		if "_" not in self.display:
			return True
		else:
			return False	


	#iterate collection of Character to allow a guess to be checked
	def check_guess(self, guess_letter):
		print("\n")
		if guess_letter.lower() not in [char.lower() for char in self.guess_letter]: #check if letter is guessed previously or not
			if super().guess_correctly(guess_letter): #check if guess is correct or not
				self.guess_letter.append(guess_letter.lower()) #saves the attempted guess letter
				self.show_letters(guess_letter, True) #update display
				return True
			else:
				self.guess_letter.append(guess_letter.lower()) #saves the attempted guess letter
				print("WRONG!")
				return False
		else:
			print("You already guess that letter!")
			return True


	#ask character object how it should show it's letter
	def show_letters(self, guess_letter=None, guess_is_correct=False):
		temp_display = []

		for char in self.phrase_letters:
			if guess_is_correct and char.lower() == guess_letter.lower():
				# print(char, end=" ")
				temp_display.append(char)
			else:
				if char == " ":	
					# print("", end=" ")
					temp_display.append(" ")
				elif char.lower() in self.guess_letter:
					# print(char, end=" ")
					temp_display.append(char)
				else:
					# print("_", end=" ")
					temp_display.append("_")

		print(" ".join(temp_display))
		self.display = temp_display



