import sys
import random

list_of_words = sys.argv[1:]


def shuffle_words():
    random.shuffle(list_of_words)


if __name__ == "__main__":
    shuffle_words()
    print(*list_of_words)
