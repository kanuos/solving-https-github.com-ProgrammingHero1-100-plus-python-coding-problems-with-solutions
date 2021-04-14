import random
from GetEnglishDictionary import get_all_words


# Word hangman [Premium]
#
# The word hangman is a simple game. You will provide a word with the first letter.
# Rest of the letters will be blank. For example,
# s_ _ _ _ _ _ _ _ _
# The player has to guess the letters in the word.
# And the player will guess one letter at a time.
# If the letter exists in the word, it will appear to the player.
# If the letter does not exist in the word, it will be counted as a wrong try.
# If the player exceeds the number of the wrong tries, the player will lose.
# Otherwise, the player will win.


class Hangman:
    def __init__(self, length):
        if length <= 0 or length > 10:
            raise ValueError("Length of word must be between 1 and 10")
        self.length = length
        self.__word = Hangman.__generate_word(length)
        self.lives_left = 5
        self.guesses = ["_ "] * length

    @staticmethod
    def __generate_word(n):
        words = {x for x in get_all_words() if len(x) == n}
        return random.choice(list(words))

    def play(self):
        if self.lives_left == 0:
            raise ValueError(f"Game over. "
                             f"\nYou guessed   {''.join(self.guesses)}. "
                             f"\nOriginal word {self.word}")
        if "".join(self.guesses) == self.word:
            raise ValueError(f"You win with {self.lives_left} heart(s)"
                             f"\nOriginal word {self.word}")
        char = input("Guess a letter : ")
        if char in self.word:
            if char not in self.guesses:
                for i, c in enumerate(self.word):
                    if c == char:
                        self.guesses[i] = char
                return
            else:
                self.lives_left -= 1
                raise ValueError(f"You have already guessed {char} before. Lives left : {self.lives_left}")
        self.lives_left -= 1
        print(f"{char} is not in the word. Lives left : {self.lives_left}")

    @property
    def word(self):
        return self.__word


try:
    print("WELCOME TO THE HANGMAN GAME")
    size = int(input("Enter the length of THE word : "))
    game = Hangman(size)
    while game.lives_left >= 0:
        print("Word : ", "".join(game.guesses))
        game.play()
except ValueError as err:
    print(err)
