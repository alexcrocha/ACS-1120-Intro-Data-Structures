import sys
import random


def generate_random_sentence(word_number):
    """
    Reads a list of words from dictionary and
    returns a random sentence with the given number of words.
    """

    with open("/usr/share/dict/words") as f:
        words = f.read().split()

    random_words = random.sample(words, k=word_number)
    return " ".join(random_words).capitalize() + "."


if __name__ == "__main__":
    number_of_words = int(sys.argv[1])
    print(generate_random_sentence(number_of_words))
