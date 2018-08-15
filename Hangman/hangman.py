from builtins import print
from random import randint
import sqlite3

connection = sqlite3.connect('words.db')
cursor = connection.cursor()
print(cursor)
connection.close()

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = open("words.txt", "r").read().splitlines()


def play():
    word = words[randint(0, len(words) - 1)]
    word_lower = word.lower()
    alive = True
    guesses = []
    tries = 0
    hint = list("_" * len(word))
    print(*hint)

    while alive:
        letter = input("Letter: ").lower()
        if len(letter) != 1:
            print("Invalid input")
            continue
        if letter in guesses:
            print("You already tried that letter!")
        else:
            if letter in word_lower:
                index = 0
                while index < len(word_lower):
                    index = word_lower.find(letter, index)
                    if index == -1:
                        break
                    hint[index] = word[index]
                    index += 1
                print(*hint)
                if "_" not in hint:
                    alive = False
                    print("You Won!")
            else:
                print(hangman[tries])
                print(*hint)
                if tries == 6:
                    alive = False
                    print("You lost\nThe word was " + word)
                tries += 1
            guesses.append(letter)
    print()
    if input("Play again? (y/n): ").lower() == "n":
        print("Goodbye!")
    else:
        play()


play()
