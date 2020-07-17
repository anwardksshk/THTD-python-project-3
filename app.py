from phrasehunter import game


my_game = None
my_phrases = [
    'Happy Thoughts', 
    'Create your own sunshine', 
    'When one door opens another one closes', 
    'Stay Positive', 
    'Anything is possible'
]


def play_phrasehunter():
    my_game = game.Game(phrases=my_phrases)
    my_game.start_game()


def play_again():
    while True:
        option = input("\nWould you like to play again? (Y/N) ")
        if option.lower() == 'y':
            play_phrasehunter()
            continue
        elif option.lower() == 'n':
            print("\nThank you for playing! Goodbye :)")
            break
        else:
            print("\nUh-Oh, Please enter either 'Y' or 'N' to continue.")


#===================================MAIN PROGRAM===================================
if __name__ == '__main__':
    play_phrasehunter()
    play_again()
