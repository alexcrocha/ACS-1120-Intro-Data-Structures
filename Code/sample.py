import random
from histogram import histogram

def generate_word(sentence):
    """
    Generates a random word from the given sentence
    """
    words_histogram = histogram(sentence)
    # pick a random word from the histogram weighted by frequency
    random_word = random.choices(
        list(words_histogram.keys()),
        weights=words_histogram.values(),
        k=1
    )[0]

    return random_word


if __name__ == "__main__":
    sentence = "one fish two fish red fish blue fish"
    words_frequency = {}
    for _ in range(10000):
        generated_word = generate_word(sentence)
        if generated_word in words_frequency:
            words_frequency[generated_word] += 1
        else:
            words_frequency[generated_word] = 1
    for word in words_frequency:
        print(f"{word}: {words_frequency[word]}")