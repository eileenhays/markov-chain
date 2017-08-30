"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    filename = open(file_path)
    return filename.read()

def make_chains(text_string, n):
    """Take input text as string for n-length grams; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text. n argument allows user to designate the length as n-gram.

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

    #split the string into list of words
    words_list = text_string.split()

    #make the keys as tuple of n-grams
    for idx in range(len(words_list)-n):    #words[idx] = word + "\n"
        key = []
        j = 0
        while j < n:   #create n-length grams keys
            key.append(words_list[idx+j])
            j += 1

        key = tuple(key) #turn key into a tuple

        if key not in chains: #add new keys without value to dictionary
            chains[key] = []

        chains[key].append(words_list[idx+n]) #add new key with values into dict

    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    punctuation = [".", ",", "!", "?", ";", ":"]

    curr_ngram = choice(chains.keys()) #picks random bigram key
    words.extend(curr_ngram)

    while curr_ngram in chains: #there is a curr_value in the dictionary:
        curr_key = curr_ngram[1:]
        curr_value = choice(chains[curr_ngram]) #randomly selects curr_value
        curr_ngram = curr_key + (curr_value,) #updates the curr_ngram variable
        words.append(curr_ngram[-1])

    gen_text = " ".join(words)#long string of generated text

    return gen_text



file_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Get a Markov chain
n = 4
chains = make_chains(input_text,n)
# print chains
# # Produce random text
random_text = make_text(chains)

print random_text
