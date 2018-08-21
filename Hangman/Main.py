from builtins import print
from random import randint

from Game import Game
from Words import Words

WORDS = Words()


class Main(object):
    def main(self):
        self.menu()

    def menu(self):
        while True:
            print("-------------------------------------------")
            print("Welcome to Hangman.py")
            print("-------------------------------------------")
            print("1) Play")
            print("2) Add a word")
            print("x) Exit")
            print("-------------------------------------------")
            choice = input("What do you want to do? ")
            if choice == '1':
                self.play()
            elif choice == '2':
                self.add()
            elif choice.lower() == 'x':
                print("Goodbye!")
                print("-------------------------------------------")
                break
            else:
                print("-------------------------------------------")
                print("Invalid input")

    def play(self):
        while True:
            print("-------------------------------------------")
            print("Play")
            print("-------------------------------------------")
            print("If you don't want to choose you can leave it blank")
            language = input("Language? (en, de, es): ")
            difficulty = input("Difficulty? (1-5): ")
            print("-------------------------------------------")

            words = self.get_words(language, difficulty)

            while True:
                x = randint(0, len(words) - 1)
                game = Game(words[x][0])
                print("Language:", words[x][1])
                game.play()
                if input("Do you want to keep playing with these settings? (y/n): ").lower() == 'n':
                    break

            if input("Do you want to keep playing with different settings? (y/n): ").lower() == 'n':
                break

    def add(self):
        while True:
            print("-------------------------------------------")
            print("Add a word")
            print("-------------------------------------------")
            print("1) Add a word")
            print("2) Add multiple words through external file")
            print("x) Exit to main menu")
            print("-------------------------------------------")
            choice = input("What do you want to do? ")
            print("-------------------------------------------")
            if choice == '1':
                word = input("Word: ")
                language = input("Language of the word: ")
                WORDS.add_word(word, language)
            elif choice == '2':
                file = input("Location of the file: ")
                language = input("Language of the words: ").lower()
                WORDS.add_file(file, language)
            elif choice.lower() == 'x':
                break
            else:
                print("Invalid input")
                print("-------------------------------------------")

    def get_words(self, language, difficulty):
        if language in ('en', 'de', 'es'):
            if difficulty in ('1', '2', '3', '4', '5'):
                return WORDS.get_word(language, difficulty)
            else:
                return WORDS.get_word(language)
        else:
            if difficulty in ('1', '2', '3', '4', '5'):
                return WORDS.get_word('%', difficulty)
            else:
                return WORDS.get_word()


if __name__ == "__main__":
    Main().main()
