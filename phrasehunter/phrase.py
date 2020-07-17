from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase #a list of string of the phrases
        self.characters_in_phrase = [Character(char) for char in phrase]


    def is_guessed(self):
        for x in self.characters_in_phrase:
            if x.get_guessed() == False:
                return False
        return True


    def check_guess(self, guess=None):
        correct_guess = False
        for x in self.characters_in_phrase:
            if x.match_guess(guess):
                correct_guess = True
            else:
                continue
        return correct_guess


    def show_display(self):
        for x in self.characters_in_phrase:
            x.show_char()