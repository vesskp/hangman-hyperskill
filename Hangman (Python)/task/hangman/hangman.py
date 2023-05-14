# Write your code here
import random
import string

attempts = 8
print(f"H A N G M A N  # {attempts} attempts")


def print_word(word, letters):
    for let in word:
        if let in letters:
            print(let, end="")
        else:
            print("-", end="")
    print()


words = ["python", "java", "swift", "javascript"]
won = 0
lost = 0
while True:
    cmd = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if cmd == "play":
        attempt = attempts
        sel_word = random.choice(words)
        found_letters = []
        guessed_letters = []
        found = False
        while attempt > 0 and not found:
            print()
            print_word(sel_word, found_letters)
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("Please, input a single letter.")
            elif letter not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            else:
                if letter in guessed_letters:
                    print("You've already guessed this letter.")
                else:
                    guessed_letters.append(letter)
                    if letter in found_letters:
                        print("No improvements.")
                    elif letter in sel_word:
                        found_letters.append(letter)
                    else:
                        print("That letter doesn't appear in the word.")
                        attempt -= 1
                    found = sorted((set(sel_word))) == sorted(found_letters)
        if found:
            print(sel_word)
            print(f"You guessed the word {sel_word}!")
            print("You survived!")
            won += 1
        else:
            print("You lost!")
            lost += 1
    elif cmd == 'results':
        print(f"You won: {won} times")
        print(f"You lost: {lost} times")
    elif cmd == 'exit':
        break
