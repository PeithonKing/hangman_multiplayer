from flask import Flask, request
from utils import Game

app = Flask(__name__)

games = {
    # 'random_uid1': Game() instance
    # 'random_uid2': Game() instance
    # ...
}

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
    if len(guesses) == 7: return game.word
    return game.construct()

app.run(debug=True, host='127.0.0.1', port=5000)