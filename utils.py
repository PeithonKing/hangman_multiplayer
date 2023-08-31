import secrets
import string

def make_uid(length = 6):
    characters = string.ascii_letters + string.digits
    chars = [secrets.choice(characters) for _ in range(length)]
    random_string = ''.join(chars)
    return random_string

class Game:
    def __init__(self, word, uid = None, guesses = []):
        self.uid = uid if uid else make_uid()
        self.word = word
        self.guesses = guesses
    def construct(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guesses: displayed_word += letter
            else: displayed_word += '_'
        return displayed_word

def check_word(word: str):
    with open("wordlist.txt") as wordfile:
        return word.lower() in [x.strip() for x in wordfile.readlines()]
