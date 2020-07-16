# Import your Game class
from phrasehunter import game

# Create your Dunder Main statement.
#===================================MAIN PROGRAM===================================
if __name__ == '__main__':
# Inside Dunder Main:
## Create an instance of your Game class
	game = game.Game(phrase=['Python', 'Javascript', 'Web Design'])
## Start your game by calling the instance method that starts the game loop
	game.start_game()
