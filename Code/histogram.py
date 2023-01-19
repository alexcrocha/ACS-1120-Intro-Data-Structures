sentence = "one fish two fish red fish blue fish"


def histogram(source_text):
    """
    Takes a source_text argument (can be either a filename or the contents of the file as a string, your choice)
    and returns a histogram of all words and the number of times they appear.
    """
    histogram = {}
    list_of_words = source_text.split()
    for word in list_of_words:
        histogram[word] = list_of_words.count(word)
    return histogram



def unique_words(histogram):
    """
    That takes a histogram argument and returns the total count of unique words in the histogram.

    """
    return len(histogram)


def frequency(word, histogram):
    """
    Takes a word and histogram argument and returns the number of times that word appears in a text.

    """
    return histogram[word]


if __name__ == "__main__":
    my_histogram = histogram(sentence)
    print(my_histogram)
    print(unique_words(my_histogram))
    print(frequency('fish', my_histogram))