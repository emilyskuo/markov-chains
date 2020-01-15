"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    combined_input_text = ""

    for arg in argv[1:]:
        text_file = open(arg)
        new_text = (text_file.read())
        new_text = new_text.rstrip()
        combined_input_text += new_text


    return combined_input_text


def make_chains(text_string, n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.split()

    for idx in range(len(text_string)-n_gram):
        key_ngram_tuple = tuple(text_string[idx:idx+n_gram])
        value_for_ngram_tuple = text_string[idx+n_gram]

        if chains.get(key_ngram_tuple) is None:
            chains[key_ngram_tuple] = [value_for_ngram_tuple]
        else:
            chains[key_ngram_tuple].append(value_for_ngram_tuple)


    return chains


def make_text(chains):
    """Return text from chains."""

    word_chain = []

    # Choose a random tuple to start the chain
    list_of_chains_keys = list(chains.keys())
    current_key = choice(list_of_chains_keys)
    word_chain.extend(list(current_key))

    while current_key in chains:

        new_word = choice(chains[current_key])
        word_chain.append(new_word)

        current_key = tuple(word_chain[-2:])

    return " ".join(word_chain)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file()

# Get a Markov chain
chains = make_chains(input_text, 3)

print(chains)
# Produce random text
# random_text = make_text(chains)

# print(random_text)
