import re

def read_file(file_name):
    """
    Reads given source file and returns list of words
    """
    with open(file_name) as f:
        words = re.findall(r"\w+", f.read().lower())
    return words