HANGMAN = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


class InvalidLetter(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class Repetition(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class WrongLetter(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class Game(object):
    def __init__(self, word):
        self.word = word
        self.word_lower = word.lower()
        self.alive = True
        self.guesses = []
        self.tries = 0
        self.hint = list("_" * len(word))

    def play(self):
        while self.alive:
            self.guess_letter(input("Letter: ").lower())

    def guess_letter(self, letter):
        try:
            if len(letter) != 1:
                raise InvalidLetter('\"' + letter + '\" is not valid', '2')
            elif letter in self.guesses:
                raise Repetition('You already tried the letter \"' + letter + '\"', '2')
            else:
                if letter in self.word_lower:
                    index = 0
                    while index < len(self.word_lower):
                        index = self.word_lower.find(letter, index)
                        if index == -1:
                            break
                        self.hint[index] = self.word[index]
                        index += 1
                    print(*self.hint)
                    if "_" not in self.hint:
                        self.alive = False
                        print("You Won!")
                        print("-------------------------------------------")
                else:
                    raise WrongLetter("message", "error")
        except InvalidLetter as e:
            print(e)
        except Repetition as e:
            print(e)
        except WrongLetter as e:
            print(self.get_hangman())
            print(*self.get_hint())
            if self.tries == 6:
                self.alive = False
                print("You lost\nThe word was " + self.word)
                print("-------------------------------------------")
            self.tries += 1
            self.guesses.append(letter)

    def get_hangman(self):
        return HANGMAN[self.tries]

    def get_hint(self):
        return self.hint
        pass
