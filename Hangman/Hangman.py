from builtins import print
from random import randint
import sqlite3
import os

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
LANGUAGES = {
    'en': ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b",
           "v", "k", "j", "x", "q", "z"],
    'de': ["e", "n", "i", "r", "t", "s", "a", "h", "d", "u", "c", "l", "g", "m", "o", "b", "f", "w", "z", "k",
           "v", "p", "ü", "ä", "ö", "j", "x", "q", "y"],
    'es': ["e", "a", "r", "o", "s", "t", "n", "i", "d", "l", "c", "t", "u", "m", "p", "b", "g", "v", "ó", "y",
           "q", "h", "f", "z", "í", "j", "á", "ñ", "é", "x", "ú", "ü", "k", "w", "î"]
}


# This exception is raised whenever a user tries to add a word to the database that contains an invalid character
class InvalidCharacter(Exception):
    def __init__(self, message, errors):
        if message == '':
            message = 'Invalid character: "%s"' % errors
        super().__init__(message)

        self.errors = errors


# This exception is raised whenever a user tries to access an invalid language
class InvalidLanguage(Exception):
    def __init__(self, message, errors):
        if message == '':
            message = 'Invalid Language: "%s"' % errors
        super().__init__(message)

        self.errors = errors


# This exception is raised whenever a user tries to open a non-existing file
class NotAFile(Exception):
    def __init__(self, message, errors):
        if message == '':
            message = '"%s" doesn\'t exist' % errors
        super().__init__(message)

        self.errors = errors


# This exception is raised whenever a user tries to enter something other than a letter
class InvalidLetter(Exception):
    def __init__(self, message, errors):
        if message == '':
            message = 'Invalid input: "%s"' % errors
        super().__init__(message)

        self.errors = errors


# This exception is raised whenever a user enters a letter he already entered
class Repetition(Exception):
    def __init__(self, message, errors):
        if message == '':
            message = 'You already tried "%s"' % errors
        super().__init__(message)

        self.errors = errors


# This exception is raised whenever a user enters a letter that isn't in the word he's trying to guess
class WrongLetter(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


# All the menus are located in this class
class Main(object):
    # This method runs the main menu
    def main(self):
        self.menu()

    # In the main menu you can choose if you want to play a game, add a word, or end the program
    def menu(self):
        while True:
            print("-------------------------------------------------------------")
            print("Welcome to Hangman")
            print("-------------------------------------------------------------")
            print("1) Play")
            print("2) Add a word")
            print("x) Exit")
            print("-------------------------------------------------------------")
            choice = input("What do you want to do? ")
            if choice == '1':
                self.play()
            elif choice == '2':
                self.add()
            elif choice.lower() == 'x':
                print("Goodbye!")
                print("-------------------------------------------------------------")
                break
            else:
                print("-------------------------------------------------------------")
                print("Invalid input")

    # In this method an instance of the game class gets created and executed
    def play(self):
        while True:
            print("-------------------------------------------------------------")
            print("Play")
            print("-------------------------------------------------------------")
            print("If you don't want to choose you can leave it blank")
            language = input("Language? (en, de, es): ")
            difficulty = input("Difficulty? (1-5): ")
            print("-------------------------------------------------------------")

            words = self.get_words(language, difficulty)

            while True:
                x = randint(0, len(words) - 1)
                game = Game(words[x][0])
                print("Language:", words[x][1])
                game.play()
                # For faster usage, you don't have to type 'y' to continue, you can just hit enter
                if input("Do you want to keep playing with these settings? (y/n): ").lower() == 'n':
                    break

            if input("Do you want to keep playing with different settings? (y/n): ").lower() == 'n':
                break

    # In this class you add a word
    def add(self):
        while True:
            print("-------------------------------------------------------------")
            print("Add a word")
            print("-------------------------------------------------------------")
            print("1) Add a word")
            print("2) Add multiple words through external file")
            print("x) Exit to main menu")
            print("-------------------------------------------------------------")
            choice = input("What do you want to do? ")
            print("-------------------------------------------------------------")
            if choice == '1':
                word = input("Word: ")
                language = input("Language of the word: ")
                try:
                    if language not in LANGUAGES:
                        raise InvalidLanguage('', language)
                    Words().add_word(word, language)
                except InvalidLanguage as e:
                    print(e)
            elif choice == '2':
                file = input("Location of the file: ")
                language = input("Language of the words: ").lower()
                try:
                    Words().add_file(file, language)
                except NotAFile as e:
                    print(e)
                except InvalidLanguage as e:
                    print(e)
            elif choice.lower() == 'x':
                break
            else:
                print("Invalid input")
                print("-------------------------------------------------------------")

    # If the language and difficulty are valid every word that matches them gets filtered out
    def get_words(self, language, difficulty):
        if language in LANGUAGES:
            if difficulty in ('1', '2', '3', '4', '5'):
                print("-------------------------------------------------------------")
                return Words().get_word(language, difficulty)
            else:
                print("Invalid difficulty, a random one will be selected")
                print("-------------------------------------------------------------")
                return Words().get_word(language)
        else:
            print("Language wasn't recognized, a random one will be selected")
            if difficulty in ('1', '2', '3', '4', '5'):
                print("-------------------------------------------------------------")
                return Words().get_word('%', difficulty)
            else:
                print("Invalid difficulty, a random one will be selected")
                print("-------------------------------------------------------------")
                return Words().get_word()


# This class communicates with the database where the words are stored
class Words(object):
    # This method executes SQL commands according to the parameters command and values
    def run_sql(self, command, values):
        connection = sqlite3.connect("words.db")
        cursor = connection.cursor()
        cursor.execute(command, values)
        words = cursor.fetchall()
        connection.commit()
        connection.close()
        return words

    # This method adds a word to the database
    def add_word(self, word, language):
        try:
            self.run_sql('INSERT INTO words VALUES (NULL, ?, ?, ?)',
                         (word, language, self.set_difficulty(word, language)))
            print("Word added")
        except InvalidCharacter as e:
            print(e)

    # This method returns every word that has the language and difficulty that were given as parameters
    def get_word(self, language='%', difficulty='%'):
        return self.run_sql('SELECT Word, Language FROM words WHERE Language LIKE ? AND Difficulty LIKE ?',
                            (language, difficulty))

    # This method calculates the difficulty of the words according to the frequency of each letter
    def set_difficulty(self, word, language):
        difficulty = 0

        if language == 'de':
            word = word.replace('ß', 'ss')

        for i in range(len(word)):
            if word[i].lower() in LANGUAGES[language]:
                difficulty += LANGUAGES[language].index(word[i].lower())
            else:
                raise InvalidCharacter('', word[i])
        difficulty = round(difficulty / len(word) / 5)
        # difficulty = round(5 / len(languages[language]) * (difficulty / len(word)))
        if difficulty > 5:
            difficulty = 5
        if difficulty < 1:
            difficulty = 1
        return difficulty

    # This method adds every word in a file to the database
    def add_file(self, file, language):
        if not os.path.isfile(file):
            raise NotAFile('', file)
        if language not in LANGUAGES:
            raise InvalidLanguage('', language)
        words = open(file, "r", encoding="utf-8").read().splitlines()
        percentage = 100 / len(words)
        for i in range(0, len(words)):
            if words[i] == '':
                continue
            self.add_word(words[i], language)
            # print(str(percentage * i) + '%', end='\r')


# This class executes the game itself
class Game(object):
    def __init__(self, word):
        self.word = word
        self.word_lower = self.remove_special_chars(word.lower())
        self.alive = True
        self.guesses = []
        self.tries = 0
        self.hint = list("_" * len(word))

    # In this method special characters like ä, ö and ü get replaced with their according vowels
    def remove_special_chars(self, word):
        letters = {
            'ü': 'u',
            'ä': 'a',
            'ö': 'o',
            'ó': 'o',
            'í': 'i',
            'á': 'a',
            'ñ': 'n',
            'é': 'e',
            'ú': 'u',
            'î': 'i'
        }
        for i in letters:
            word = word.replace(i, letters[i])
        return word

    # This loop keeps going as long as the game is not over yet
    def play(self):
        print(*self.get_hint())
        while self.alive:
            self.guess_letter(self.remove_special_chars((input("Letter: ").lower())))

    # This method validates the user's input
    def guess_letter(self, letter):
        try:
            if len(letter) != 1:
                raise InvalidLetter('', letter)
            elif letter in self.guesses:
                raise Repetition('', letter)
            else:
                self.guesses.append(letter)
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
                        print("-------------------------------------------------------------")
                else:
                    raise WrongLetter("message", "error")
        except InvalidLetter as e:
            print(e)
        except Repetition as e:
            print(e)
        except WrongLetter:
            print(self.get_hangman())
            print(*self.get_hint())
            if self.tries == 6:
                self.alive = False
                print("You lost\nThe word was " + self.word)
                print("-------------------------------------------------------------")
            self.tries += 1

    # This method returns the current state of hang man
    def get_hangman(self):
        return HANGMAN[self.tries]

    # This method returns every guessed letter
    def get_hint(self):
        return self.hint


if __name__ == "__main__":
    Main().main()
