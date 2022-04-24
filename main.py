import string

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
        self._pick_answer_word()

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

    def _update_knowledge_base(self, letter=None, pos=None, letter_state=None):
        if not self.knowledge_base:
            self.knowledge_base = [
                string.ascii_lowercase,
                string.ascii_lowercase,
                string.ascii_lowercase,
                string.ascii_lowercase,
                string.ascii_lowercase,
            ]
            return
        if letter_state == self.COLOR_UNUSED_LETTER:
            for i in range(5):
                self.knowledge_base[i] = self.knowledge_base[i].replace(letter, '')
        elif letter_state == self.COLOR_USED_LETTER:
            self.knowledge_base[pos] = self.knowledge_base[pos].replace(letter, '')
        elif letter_state == self.COLOR_CORRECT_LETTER_AND_POS:
            self.knowledge_base[pos] = letter
        print("Updated KB: " + str(self.knowledge_base))

    def _update_possible_words(self):
        if not self.possible_words:
            with open("words.txt") as f:
                self.possible_words = f.read().split("\n")

    @classmethod
    def _is_word_valid(cls, word):
        if len(word) == 5:
            with open("words.txt") as f:
                return word in f.read().split("\n")
        return False


if __name__ == '__main__':
    game = Wordle()



