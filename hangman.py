"""
Hangman
"""
import datetime
print(__doc__)

guess_word = "andrejko"
guess_count = len(guess_word)
guess = "-"*guess_count
start = datetime.datetime.now()

while guess_count != 0 and guess_word != guess:
    letter = input("Zadej znak: ")[0]

    if letter in guess_word:
        index_letter = guess_word.find(letter)
        guess = guess[:index_letter] + letter + guess[index_letter + 1:]
        print(guess)
    else:
        guess_count = guess_count-1
        print(f"Mas {guess_count} pokusu.")

finish = datetime.datetime.now() - start

if guess_word == guess:
    print(f"\nGratuluji, vyhral jsi. Tvuj cas je {finish}.")
else:
    print(f"\nProhral jsi. Slovo bylo {guess_word}.")
