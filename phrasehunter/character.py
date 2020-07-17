class Character:
	def __init__(self, original, was_guessed=False):
		self.original = original
		if self.original == " ":
			self.was_guessed = True
		else:
			self.was_guessed = was_guessed


	def __str__(self):
		return "The char {} has boolean {}".format(self.original, self.was_guessed)


	def match_guess(self, user_guess=None):
		if user_guess.lower() == self.original.lower():
			self.was_guessed = True
			return True
		else:
			return False


	def show_char(self):
		for char in self.original:
			if self.was_guessed == True:
				print(self.original, end=" ")
			elif char == " ":
				print("", end=" ")
			else:
				print("_", end=" ")


	def get_guessed(self):
		return self.was_guessed