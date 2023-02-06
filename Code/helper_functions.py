import re


def read_file(file_name):
    """
    Reads given source file and returns list of words
    """
    with open(file_name) as f:
        words = re.findall(r"\b\w+(?:[-']\w+)?\b", f.read().lower())
    return words
