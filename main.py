from wordle import wordle
import random
from rich.console import Console
import sys


def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words
    



def main():
    console = Console()

    secret_word = load_dictionary("answers.txt")
    secret_word = random.choice(secret_word)
    
    guesses = load_dictionary("guesses.txt")
    
    game  = wordle(secret_word, guesses)

    while game.can_attempt():
        print("You have {} attempts left to guess the 5 letter word".format(game.attempts_left()))
        guess =  input("Enter a 5 letter word: ")
        if game.valid_guess_length(guess) == False:
            print("Make sure your guess is 5 letters long")
            continue
        if game.valid_guess(guess) == False:
            print("Make sure your guess is a real word")
            continue
        
        game.format_guess(guess)

        for i in game.prev_attempts:
            console.print(i)

        if game.is_winner(guess) == True:
            print("You got the word correct in {} attempts".format(len(game.prev_attempts)))
            sys.exit()
    
    print("No more attempts left. The secret word was {}.".format(secret_word))
    sys.exit()


if __name__ == "__main__":
    main()