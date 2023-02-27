from dictogram3 import Dictogram
from helper_functions import read_file

words_histogram = {}

# def generate_markov(source_text, number=1):
#     """
#     Generates a random sentence from the given text and word count number
#     """

#     words_histogram["filled"] = (
#         Dictogram(source_text)
#         if len(words_histogram) == 0
#         else words_histogram["filled"]
#     )

#     histogram = words_histogram["filled"]
#     word_list = []
#     word_list.append(histogram.sample_start())
#     for _ in range(number):
#         word_list.append(histogram.sample_next(word_list[-1]))
#         while word_list[-1][-1] not in [".", "!", "?"]:
#             word_list.append(histogram.sample_next(word_list[-1]))
#     return " ".join(word_list)

def genereate_n_order_markov(source_text, sentence_number=1, order=1):
    """
    Generates a random sentence from the given text and word count number
    """

    words_histogram["filled"] = (
        Dictogram(source_text, order)
        if len(words_histogram) == 0
        else words_histogram["filled"]
    )

    histogram = words_histogram["filled"]
    tuple_list = []
    tuple_list.append(histogram.sample_start())

    for _ in range(sentence_number):
        tuple_list.append(histogram.sample_next(tuple_list[-1]))
        while tuple_list[-1][-1][-1] not in [".", "!", "?"]:
            tuple_list.append(histogram.sample_next(tuple_list[-1]))
    word_list = []
    for index in range(len(tuple_list)):
            word_list.append(tuple_list[index][-1])
    return " ".join(word_list)



if __name__ == "__main__":
    text = read_file("./data/sample.txt")
    print(generate_markov(text, 5))
