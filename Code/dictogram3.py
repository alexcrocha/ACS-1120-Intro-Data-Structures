#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None, order=1):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        self.order = order
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for index in range(len(word_list)):
                self.add_count(tuple(word_list[index: index + order]))
                if index + order <= len(word_list) - order:
                    self.add_next(tuple(word_list[index: index + order]), tuple(word_list[index+1: index + order +1]))

    def add_count(self, word_tuple, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increase word frequency by count
        if word_tuple in self:
            self[word_tuple]["count"] += count
        else:
            self[word_tuple] = {"count": count, "next": {}}
            self.types += 1
        self.tokens += count

    def add_next(self, word_tuple, next_tuple):
        if next_tuple in self[word_tuple]["next"]:
            self[word_tuple]["next"][next_tuple] += 1
        else:
            self[word_tuple]["next"][next_tuple] = 1

    def frequency(self, word_tuple):
        """Return frequency count of given word, or 0 if word is not found."""
        # Retrieve word frequency count
        return self[word_tuple]["count"] if word_tuple in self else 0

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # Randomly choose a word based on its frequency in this histogram

        dart = random.uniform(0, self.tokens)
        fence = 0
        for word_tuple in self:
            fence += self[word_tuple]["count"]
            if dart <= fence:
                return word_tuple

    def sample_start(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # Randomly choose a word based on its frequency in this histogram
        start_histogram = {}
        start_tokens = 0
        for word_tuple in self:
            if word_tuple[-1][-1] in [".", "!", "?"]:
                next_tuples = self[word_tuple]["next"]
                for next_tuple in next_tuples:
                    if next_tuple in start_histogram:
                        start_histogram[next_tuple] += next_tuples[next_tuple]
                    else:
                        start_histogram[next_tuple] = next_tuples[next_tuple]
                    start_tokens += next_tuples[next_tuple]

        dart = random.uniform(0, start_tokens)
        fence = 0
        for word_tuple in start_histogram:
            fence += start_histogram[word_tuple]
            if dart <= fence:
                return word_tuple

    def sample_next(self, word_tuple):
        next_tuples = self[word_tuple]["next"]

        next_histogram = {}
        next_tokens = 0

        for word_tuple in next_tuples:
            if word_tuple in next_histogram:
                next_histogram[word_tuple] += next_tuples[word_tuple]
            else:
                next_histogram[word_tuple] = next_tuples[word_tuple]
            next_tokens += next_tuples[word_tuple]

        dart = random.uniform(0, next_tokens)
        fence = 0
        for word_tuple in next_histogram:
            fence += next_histogram[word_tuple]
            if dart <= fence:
                return word_tuple


def print_histogram(word_list):
    print()
    print("Histogram:")
    print("word list: {}".format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print("dictogram: {}".format(histogram))
    print("{} tokens, {} types".format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print("{!r} occurs {} times".format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print("Histogram samples:")
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print("samples: {}".format(samples_hist))
    print()
    print("Sampled frequency and error from observed frequency:")
    header = "| word type | observed freq | sampled freq  |  error  |"
    divider = "-" * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = "\033[32m"
    yellow = "\033[33m"
    red = "\033[31m"
    reset = "\033[m"
    # Check each word in original histogram
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count["count"] / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print(
            "| {!r:<9} ".format(word)
            + "| {:>4} = {:>6.2%} ".format(count["count"], observed_freq)
            + "| {:>4} = {:>6.2%} ".format(samples, sampled_freq)
            + "| {}{:>+7.2%}{} |".format(color, error, reset)
        )
    print(divider)
    print()


def main():
    import sys

    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = "abracadabra"
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = "one fish two fish red fish blue fish"
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = (
            "how much wood would a wood chuck chuck" " if a wood chuck could chuck wood"
        )
        print_histogram(woodchuck_text.split())


if __name__ == "__main__":
    main()
