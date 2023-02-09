from dictogram2 import Dictogram
from helper_functions import read_file


def generate_markov(source_text, number=1):
    """
    Generates a random sentence from the given text and word count number
    """
    histogram = Dictogram(source_text)
    word_list = []
    word_list.append(histogram.sample_start())
    for _ in range(number):
        word_list.append(histogram.sample_next(word_list[-1]))
        while word_list[-1][-1] not in [".", "!", "?"]:
            word_list.append(histogram.sample_next(word_list[-1]))
    return " ".join(word_list)


if __name__ == "__main__":
    text = read_file("./data/sample.txt")
    print(generate_markov(text, 5))
