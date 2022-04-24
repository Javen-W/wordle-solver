import string
import re
from termcolor import colored
from random import choice


class Wordle:
    def __init__(self):
        self.possible_words = None
        self.answer_word = None
        self.knowledge_base = None
        self.guessed_words = []

        self._update_possible_words()
        self._update_knowledge_base()
        self._pick_answer_word()
        self._start()

    COLOR_CORRECT_LETTER_AND_POS = 'green'
    COLOR_USED_LETTER = 'yellow'
    COLOR_UNUSED_LETTER = 'white'

    def _start(self):
        while len(self.guessed_words) < 6 and self.answer_word not in self.guessed_words:
            self._print_guesses()
            self._prompt_guess()

        self._print_guesses()
        if self.answer_word in self.guessed_words:
            return print("Congrats, you win! The answer was {}".format(colored(self.answer_word, 'green')))
        else:
            return print("You lose! The answer was {}".format(colored(self.answer_word, 'red')))

    def _print_guesses(self):
        for i, w in enumerate(self.guessed_words):
            output = ""
            for j, c in enumerate(w):
                output += "[{}]".format(self._get_letter_color(letter=c, letter_state=self._get_letter_state(pos=j, letter=c)))
            print(output)
        for i in range(6 - len(self.guessed_words)):
            print("[ ][ ][ ][ ][ ]")

    def _prompt_guess(self):
        guess = input("What is your guess? ")
        if not self._is_word_valid(guess):
            print("Invalid word!")
            return print()
        print()
        self.guessed_words.append(guess)
        for i, c in enumerate(guess):
            self._update_knowledge_base(
                letter=c,
                pos=i,
                letter_state=self._get_letter_state(pos=i, letter=c)
            )
            self._update_possible_words()
        print("Updated KB: " + str(self.knowledge_base))
        print("Updated possible words size: " + str(len(self.possible_words)))
        if len(self.possible_words) < 50:
            print("Possible words left: " + str(self.possible_words))

    def _get_letter_state(self, pos, letter):
        if self.answer_word[pos] == letter:
            return self.COLOR_CORRECT_LETTER_AND_POS
        if letter in self.answer_word:
            return self.COLOR_USED_LETTER
        return self.COLOR_UNUSED_LETTER

    def _get_letter_color(self, letter, letter_state):
        return colored(letter, letter_state)

    def _pick_answer_word(self):
        self.answer_word = choice(self.possible_words)
        # print("DEBUG: answer word: " + str(self.answer_word))

    def _update_knowledge_base(self, letter=None, pos=None, letter_state=None):
        if not self.knowledge_base:
            self.knowledge_base = {
                'possible_letters': [
                    string.ascii_lowercase,
                    string.ascii_lowercase,
                    string.ascii_lowercase,
                    string.ascii_lowercase,
                    string.ascii_lowercase,
                ],
                'word_must_include': []
            }
            return
        if letter_state == self.COLOR_UNUSED_LETTER:
            for i in range(5):
                self.knowledge_base['possible_letters'][i] = self.knowledge_base['possible_letters'][i].replace(letter, '')
        elif letter_state == self.COLOR_USED_LETTER:
            self.knowledge_base['possible_letters'][pos] = self.knowledge_base['possible_letters'][pos].replace(letter, '')
            self.knowledge_base['word_must_include'].append(letter)
        elif letter_state == self.COLOR_CORRECT_LETTER_AND_POS:
            self.knowledge_base['possible_letters'][pos] = letter

    def _update_possible_words(self):
        if not self.possible_words:
            with open("answer_words.txt") as f:
                self.possible_words = f.read().split(",")
        else:
            regex = r"[{}][{}][{}][{}][{}]".format(
                self.knowledge_base['possible_letters'][0],
                self.knowledge_base['possible_letters'][1],
                self.knowledge_base['possible_letters'][2],
                self.knowledge_base['possible_letters'][3],
                self.knowledge_base['possible_letters'][4],
            )
            for c in self.knowledge_base['word_must_include']:
                self.possible_words = [w for w in self.possible_words if c in w]
                # print("DEBUG: must include filtered list: " + str([w for w in self.possible_words if c in w]))
            self.possible_words = re.findall(regex, " ".join(self.possible_words))
        # print("DEBUG: possible words updated: " + str(self.possible_words))

    @classmethod
    def _is_word_valid(cls, word):
        if len(word) == 5:
            with open("guess_words.txt") as f:
                return word in f.read().split("\n")
        return False


if __name__ == '__main__':
    game = Wordle()



