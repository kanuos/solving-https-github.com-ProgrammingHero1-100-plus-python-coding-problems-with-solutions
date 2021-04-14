from GetEnglishDictionary import get_all_words
import re

# Build a simple word completion game.
# You will be given a partial word with hyphens. It’s a clue to an actual word. For example,
# -a-e
# Now you have to provide a word that matches with the exposed letters.
# If you provide any of these words- “game” or “fame” or “lame”, your answer will be correct.
#
# Because all these words have the letter “a” in the second position and the letter “e” in
# the fourth position.
# So, the idea is, your provided word has to have the same letter as the clue.

try:
    print("Use '_' underscores for wild card characters.")
    print("Spaces and other symbols are not allowed")
    pattern = input("Enter a pattern ")
    if any([c for c in pattern if not c.isalpha() and c != '_']):
        raise ValueError("Only alphabetical characters allowed")
    pattern = ".".join(pattern.split('_'))
    print("Pattern selected : ", pattern)
    words = [x for x in get_all_words() if len(x) == len(pattern) and re.match(pattern, x)]
    print(words)

except ValueError as err:
    print(err)
