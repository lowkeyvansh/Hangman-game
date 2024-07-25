import random

def get_word():
    words = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([char if char in guessed_letters else '_' for char in word])
    return display

word = get_word()
guessed_letters = set()
attempts = 6

while attempts > 0:
    print(display_word(word, guessed_letters))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        guessed_letters.add(guess)
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")
    if set(word) == guessed_letters:
        print("You won!")
        break
else:
    print(f"You lost! The word was: {word}")
