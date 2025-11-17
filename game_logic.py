from ascii_art import STAGES
import random


WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current snowman stage and the secret word with guessed letters revealed."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """
    Play a single round of Snowman Meltdown, prompting the player to guess letters.
    The game ends when the player wins or loses.
    """
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if set(secret_word) <= guessed_letters:
            print("You won!")
            return

        guess = input("Guess a letter: ").lower()
        if len(guess) == 1:
            print("You guessed:", guess)
        else:
            print("Invalid input. Please provide only one letter.")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
        else:
            mistakes += 1

        if mistakes > 3:
            print("Game over!")
            return
