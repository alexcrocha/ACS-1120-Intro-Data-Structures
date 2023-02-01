import random
from histogram import dictogram
from helper_functions import read_file

words_histogram = {}


def generate_word(source_text):
    """
    Generates a random word from the given text
    """
    words_histogram["filled"] = (
        dictogram(source_text)
        if len(words_histogram) == 0
        else words_histogram["filled"]
    )
    # pick a random word from the histogram weighted by frequency
    random_word = random.choices(
        list(words_histogram["filled"].keys()),
        weights=words_histogram["filled"].values(),
        k=1,
    )[0]

    return random_word


def generate_sentence(source_text, number):
    """
    Generates a random sentence from the given text and word count number
    """
    word_list = []
    for _ in range(number):
        word_list.append(generate_word(source_text))
    return " ".join(word_list).capitalize() + "."


if __name__ == "__main__":
    text = read_file("./data/sample.txt")
    words_frequency = {}
    for _ in range(10000):
        generated_word = generate_word(text)
        if generated_word in words_frequency:
            words_frequency[generated_word] += 1
        else:
            words_frequency[generated_word] = 1
    for word in words_frequency:
        print(f"{word}: {words_frequency[word]}")
