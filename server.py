import secrets
import string
from flask import Flask, request

app = Flask(__name__)

games = {
    # 'random_uid1': Game() instance
    # 'random_uid2': Game() instance
    # ...
}

def make_uid(length = 6):
    characters = string.ascii_letters + string.digits
    chars = [secrets.choice(characters) for _ in range(length)]
    random_string = ''.join(chars)
    return random_string

class Game:
    def __init__(self, word):
        self.uid = make_uid()
        self.word = word
        self.guesses = []
    def construct(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guesses: displayed_word += letter
            else: displayed_word += '_'
        return displayed_word
    
@app.route('/start_game/<word>')
def start_game(word):
    global games
    game = Game(word)
    games[game.uid] = game
    return game.uid
    
@app.route('/stats/<uid>')
def stats(uid):
    game = games.get(uid)
    if not game: return 'No game found'
    return game.guesses

@app.route('/guesser/<uid>')
def guesser(uid):
    game = games.get(uid)
    if not game: return 'No game found'
    return str(len(game.word))  # coz only string can be returned

@app.route('/make_move/<uid>', methods=['POST'])
def make_move(uid):
    guesses = request.json['guesses']
    game = games.get(uid)
    if not game: return 'No game found'
    game.guesses = guesses
    return game.construct()

app.run(debug=True, host='127.0.0.1', port=5000)