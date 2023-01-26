import random
from histogram import dictogram

def generate_word(source_text):
    """
    Generates a random word from the given sentence
    """
    words_histogram = dictogram(source_text)
    # pick a random word from the histogram weighted by frequency
    random_word = random.choices(
        list(words_histogram.keys()),
        weights=words_histogram.values(),
        k=1
    )[0]

    return random_word

def generate_sentence(source_text, number):
    word_list = []
    for _ in range(number):
        word_list.append(generate_word(source_text))
    return " ".join(word_list).capitalize() + "."


if __name__ == "__main__":
    sentence = "./data/volcanoes.txt"
    words_frequency = {}
    for _ in range(10000):
        generated_word = generate_word(sentence)
        if generated_word in words_frequency:
            words_frequency[generated_word] += 1
        else:
            words_frequency[generated_word] = 1
    for word in words_frequency:
        print(f"{word}: {words_frequency[word]}")