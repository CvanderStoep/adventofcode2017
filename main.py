def read_input_file(file_name: str):
    """
    Reads an input file line by line and splits each line into a list of words.
    :param file_name: Name of the file to read.
    :return: A generator yielding lists of words for each line.
    """
    try:
        with open(file_name) as f:
            return (line.split() for line in f.read().splitlines())
    except FileNotFoundError:
        raise ValueError(f"File '{file_name}' not found.")

def check_passphrase(phrase: list) -> bool:
    """
    Checks if all words in the passphrase are unique.
    :param phrase: List of words in the passphrase.
    :return: True if all words are unique, False otherwise.
    """
    return len(phrase) == len(set(phrase))

def check_passphrase_two(phrase: list) -> bool:
    """
    Checks if all words in the passphrase are unique, including when considering anagrams.
    :param phrase: List of words in the passphrase.
    :return: True if no words are anagrams or duplicates, False otherwise.
    """
    condensed_phrase = [''.join(sorted(word)) for word in phrase]
    return check_passphrase(condensed_phrase)

def compute_part(file_name: str, passphrase_function) -> str:
    """
    Computes the number of valid passphrases using the provided passphrase validation function.
    :param file_name: Name of the file containing passphrases.
    :param passphrase_function: Function used to validate each passphrase.
    :return: A string representing the count of valid passphrases.
    """
    phrases = read_input_file(file_name)
    print(phrases)
    valid_phrases = sum(1 for phrase in phrases if passphrase_function(phrase))
    return f'{valid_phrases= }'

if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input4.txt', check_passphrase)}")
    print(f"Part II: {compute_part('input/input4.txt', check_passphrase_two)}")
