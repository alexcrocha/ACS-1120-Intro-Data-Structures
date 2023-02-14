import re


def read_file(file_name):
    """
    Reads given source file and returns list of words
    """
    with open(file_name) as f:
        words = re.findall(r"[a-zA-Z_.',:-;!?]+", f.read())

    for index, word in enumerate(words):
        if validate_word(word) is False:
            words.pop(index)

    return words

def validate_word(word):
    """
    Returns True if word is valid, False otherwise
    """
    if len(word) == 1 and word not in ["I", "a", "A", "O"]:
        return False

    return True