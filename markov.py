"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    filename = open(file_path)
    return filename.read()

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

    #split the string into list of words
    words_list = text_string.split()

    #make the keys as tuple of bigrams
    for idx in range(len(words_list)-2):
        key = (words_list[idx], words_list[idx+1])#why doesn't this have an index error for i+1 for the last item?
        if key not in chains:
            chains[key] = []

        chains[key].append(words_list[idx+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    keys_list = chains.keys()

    first_bigram = choice(keys_list) #picks random bigram key
    words.append(first_bigram[0])
    words.append(first_bigram[1])
    value = chains[first_bigram]

    new_bigram = (first_bigram[1], choice(value))

    while new_bigram in chains: #there is a value in the dictionary:
        key = new_bigram[1]
        value = choice(chains[new_bigram]) #randomly selects value

        new_bigram = (key, value) #updates the new_bigram variable
        words.append(new_bigram[0])

    words.append(new_bigram[1]) #add the last word on

    # for idx, word in words.items(): #add a line break after a "?"
    #     for char in word:
    #         if char == "?":
    #             words[idx] = word + "\n"

    # print words
    gen_text = " ".join(words)#long string of generated text

    return gen_text


# input_path = "green-eggs.txt"
# input_path = "gettysburg.txt"
input_path = "somewhere-over-rainbow.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print random_text
