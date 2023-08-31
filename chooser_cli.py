import requests
from utils import Game, check_word
import time

IP = "127.0.0.1"
PORT = 5000

while True:
    word = input("Enter the word: ").lower()
    if check_word(word):
        break
    else:
        print("Invalid word. Try again.")

# send a get request to 'start_game/<word>' endpoint
ID = requests.get(f"http://{IP}:{PORT}/start_game/{word}").text

print(f"Your game ID is: {ID}")
print("Share this ID with the guesser.\nWaiting for him to join...")

game = Game(word, ID)

# then every 5 seconds send a request to 'stats/<id>' with the id to get
# a list of letters guessed by guesser.

while True:
    guess = requests.get(f"http://{IP}:{PORT}/stats/{ID}").json()
    if game.guesses != guess:
        print(f"Guesser guessed new letters: {', '.join(guess[len(game.guesses):])}")  # noqa: E501
        game.guesses = guess
        print(f"Current state of the word: {game.construct()}")
        print(f"{7 - len(game.guesses)} guesses left")
        if len(game.guesses) == 7:
            break
    time.sleep(5)

if "_" not in game.construct():
    print("Guesser won!")
else:
    print("Guesser lost!")
