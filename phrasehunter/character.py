# Create your Character class logic in here.
class Character():
	def __init__(self, original, was_guessed=False):
		self.original = original
		# self.was_guessed = was_guessed

	def guess_correctly(self, guess_char):
		for char in self.original:
			if guess_char.lower() == char.lower():
				return True


	# def show_char(self):
	# 	pass
