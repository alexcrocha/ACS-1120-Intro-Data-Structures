import re


def histogram(source_text):
    """
    Takes a source_text argument and returns a histogram of all words and the number of times they appear.
    """
    histogram = {}
    list_of_words = re.findall(r"\w+", source_text.lower())
    for word in list_of_words:
        histogram[word] = list_of_words.count(word)
    return histogram


def listogram(source_text):
    """
    Takes a source_text argument and returns a histogram of all words and the number of times they appear.
    """
    listogram = []
    list_of_words = re.findall(r"\w+", source_text.lower())
    helper_list = []
    for word in list_of_words:
        if word not in helper_list:
            listogram.append([word, list_of_words.count(word)])
            helper_list.append(word)
    return listogram


def unique_words(histogram):
    """
    Takes a histogram argument and returns the total count of unique words in the histogram.

    """
    return len(histogram)


def frequency(word, histogram):
    """
    Takes a word and histogram argument and returns the number of times that word appears in a text.

    """
    if isinstance(histogram, dict):
        return histogram[word]
    elif isinstance(histogram, list):
        for x in range(len(histogram)):
            if word in histogram[x]:
                return histogram[x][1]


if __name__ == "__main__":
    sentence = "one fish two fish red fish blue fish"
    my_histogram = histogram(sentence)
    my_listogram = listogram(sentence)
    print(my_histogram)
    print(unique_words(my_histogram))
    print(frequency("fish", my_histogram))
    print(my_listogram)
    print(unique_words(my_listogram))
    print(frequency("fish", my_listogram))
