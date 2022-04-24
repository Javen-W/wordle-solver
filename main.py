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
                output += "[{}]".format(self._get_letter_color(j, c))
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

    def _get_letter_color(self, pos, c):
        if self.answer_word[pos] == c:
            return colored(c, 'green')
        if c in self.answer_word:
            return colored(c, 'yellow')
        return colored(c, 'white')

    def _pick_answer_word(self):
        self.answer_word = choice(self.possible_words)

    def _update_knowledge_base(self):
        if not self.knowledge_base:
            return

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



