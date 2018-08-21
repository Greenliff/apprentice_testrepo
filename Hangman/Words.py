import sqlite3
import os


class InvalidCharacter(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class NotAFile(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class Words(object):

    def run_sql(self, command, values):
        connection = sqlite3.connect("words.db")
        cursor = connection.cursor()
        cursor.execute(command, values)
        words = cursor.fetchall()
        connection.commit()
        connection.close()
        return words

    def add_word(self, word, language):
        try:
            self.run_sql('INSERT INTO words VALUES (NULL, ?, ?, ?)',
                         (word, language, self.set_difficulty(word, language)))
        except InvalidCharacter as e:
            print(e)

    def get_word(self, language='%', difficulty='%'):
        return self.run_sql('SELECT Word, Language FROM words WHERE Language LIKE ? AND Difficulty LIKE ?',
                            (language, difficulty))

    def set_difficulty(self, word, language):
        languages = {
            'en': ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b",
                   "v", "k", "j", "x", "q", "z"],
            'de': ["e", "n", "i", "r", "t", "s", "a", "h", "d", "u", "c", "l", "g", "m", "o", "b", "f", "w", "z", "k",
                   "v", "p", "ü", "ä", "ö", "j", "x", "q", "y"],
            'es': ["e", "a", "r", "o", "s", "t", "n", "i", "d", "l", "c", "t", "u", "m", "p", "b", "g", "v", "ó", "y",
                   "q", "h", "f", "z", "í", "j", "á", "ñ", "é", "x", "ú", "ü", "k", "w", "î"]
        }

        difficulty = 0
        if language not in languages:
            language = 'en'

        if language == 'de':
            word = word.replace('ß', 'ss')

        for i in range(len(word)):
            if word[i].lower() in languages[language]:
                difficulty += languages[language].index(word[i].lower())
            else:
                raise InvalidCharacter('\"' + word[i] + '\" is an invalid character', '2')
        difficulty = round(difficulty / len(word) / 5)
        # difficulty = round(5 / len(languages[language]) * (difficulty / len(word)))
        if difficulty > 5:
            difficulty = 5
        if difficulty < 1:
            difficulty = 1
        return difficulty

    def add_file(self, file, language):
        try:
            if not os.path.isfile(file):
                raise NotAFile('\"' + file + '\" is an invalid file path', '2')
            words = open(file, "r", encoding="utf-8").read().splitlines()
            percentage = 100 / len(words)
            for i in range(0, len(words)):
                self.add_word(words[i], language)
                print(str(percentage * i) + '%', end='\r')
            print("Success")
        except NotAFile as e:
            print(e)
