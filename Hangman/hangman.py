from builtins import print
from random import randint
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

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

word = words[randint(0, len(words) - 1)]
alive = True
guesses = []
tries = 0
hint = list("_" * len(word))

while alive:
    letter = input("Letter: ").lower()
    if len(letter) != 1:
        print("Not a valid input")
        continue
    if letter in guesses:
        print("You already tried that letter!")
    else:
        if letter in word:
            index = 0
            while index < len(word):
                index = word.find(letter, index)
                if index == -1:
                    break
                hint[index] = letter
                index += 1
            print(*hint)
            if "_" not in hint:
                alive = False
                print("You Won!")
        else:
            print(hangman[tries])
            print(*hint)
            print()
            if tries == 6:
                alive = False
                print("You lost\nThe word was " + word)
            tries += 1
        guesses.append(letter)

