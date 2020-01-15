"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path)
    new_text = (text_file.read())
    new_text = new_text.rstrip()


    return new_text


def make_chains(text_string):
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
    # key_list = []
    # list_of_values = []

    for idx in range(len(text_string)-2):
        key_bigram_tuple = (text_string[idx], text_string[idx+1])
        # key_list.append(key_bigram_tuple)
        value_for_bigram_tuple = text_string[idx+2]

        if chains.get(key_bigram_tuple) is None:
            chains[key_bigram_tuple] = [value_for_bigram_tuple]
        else:
            chains[key_bigram_tuple].append(value_for_bigram_tuple)


    return chains
        # print(key_bigram_tuple, value_for_bigram_tuple)

    # if key_list.count(key) > 1:
    #     list_of_values.append(value_for_bigram_tuple)
    #     print(list_of_values)



    #chains[key_bigram_tuple].append(value_for_bigram_tuple)

    # else:
    #     chains[key_bigram_tuple] = value_for_bigram_tuple



    # key_list.append(key_bigram_tuple)

    # value_for_bigram_tuple = []
    # value_for_bigram_tuple.append(text_string[idx+2])

    # print(value_for_bigram_tuple)
    #chains[key_bigram_tuple] = value_for_bigram_tuple


    # key for  in chains 


    # your code goes here

    # return chains


def make_text(chains):
    """Return text from chains."""

    word_chain = []


    # your code goes here
    list_of_chains_keys = list(chains.keys())
    initial_key = choice(list_of_chains_keys)
    word_chain.extend(list(initial_key))

    print("initial", initial_key)
    print("word_chain", word_chain)




    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# print(chains)
# # # Produce random text
# random_text = make_text(chains)

# # print(random_text)
make_text(chains)