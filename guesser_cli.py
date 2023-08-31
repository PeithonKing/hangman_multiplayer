import requests

IP = "127.0.0.1"
PORT = 5000

guesses = []

while True:
    ID = input("Enter the ID shared by the chooser: ")
    length = requests.get(f"http://{IP}:{PORT}/guesser/{ID}").text
    if length.isnumeric():
        length = int(length)
        break
    else:
        print("Invalid ID. Try again.")

# make_move/<id>' (POST) sent every time a new character is guessed
# - send your ID
# - send your list of characters guessed
# - post request body should be of form: {"guesses": ["a", "b", "c", "d"]}

print(f"Word is of length: {length}")

while True:
    print(f"{7 - len(guesses)} guesses left")
    guess = input("Enter your guess: ").lower()
    if guess in guesses:
        print("You already guessed this letter. Try again.")
        continue
    guesses.append(guess)
    response = requests.post(f"http://{IP}:{PORT}/make_move/{ID}", json={"guesses": guesses}).text  # noqa: E501
    print(" ".join(list(response)))
    if len(guesses) == 7:
        break

word = ''
for letter in response:
    if letter in guesses:
        word += letter
    else:
        word += '_'

if word == response:
    print("You won!")
else:
    print("You lost!")
