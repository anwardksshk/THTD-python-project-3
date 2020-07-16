# Create your Character class logic in here.
class Character():
	def __init__(self, original, was_guessed=False):
		self.original = original
		self.was_guessed = was_guessed

	def guess_correctly(self, guess_char):
		"""
		An instance method that will take a single string 
		character guess as an argument when its called. 
		The job of this instance method is to update the 
		instance attribute storing the boolean value, 
		if the guess character is an exact match to the 
		instance attribute storing the original char passed 
		in when the Character object was created.
		"""
		for char in self.original:
			if guess_char.lower() == char.lower():
				return True


	def show_char(self):
		"""
		An instance method that when called, will show the 
		original character if the instance attribute was_guessed is True. 
		Otherwise, the instance method should show an _ or 
		underscore character to act as a hidden placeholder character.
		"""
		pass
