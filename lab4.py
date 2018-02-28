"""
lab4start.py
Mason Renehan
Updated Feb 28, 2018
Practice with sequence traversal and string processing
"""

def spell_w(word):
    """
    Prints out characters in word seperated by *** using a while loop
    word: string
    Returns: None
    """
    # define loop variable idx and initialize with 0
    idx = 0
    # write while header
    while(idx < (len(word))):
    # termination condition tests that idx is smaller than no. chars in word
        # define local variable letter to store character in word at idx
        letter = word[idx]
        # print out character in letter and end printing with ***
        print(letter, end='***')
        # advance idx to next position
        idx = idx + 1

    print( ) # print new empty line
    
spell_w('abc')

def spell_f(word):
    """
    Prints out characters in word seperated by *** using a for loop
    
    word: string
    Returns: None
    """
    
    # write for header, in which we
    # create loop variable letter to iterate through characters in word
    for letter in word:
        # print out characdter in letter and end printing with ***
        print(letter, end='***')

    print( ) # print new empty line
    
spell_f('words')

def my_len(word):
    """
    Returns the length word using string traversal and accumulator pattern
    
    word: string
    Returns: Integer value corresponding to length of word
    """

    word_len = 0 # initialize variable word_len to track length

    # loop over the word letter by letter
    for char in word:

        # accumulate 1 into word_len to count the letters
        word_len = word_len + 1
    # return word_len
    return word_len
    print ()

my_len('words')


def my_find(word, letter):
	"""
	Tests if letter is in word
	word: string
	letter: one-character string
	Returns: True if letter is in word, False otherwise
	"""
	# initialize variable found to False
	found = False
	# loop over word using a loop variable different than letter!!!

		# tests if loop variable is the same as letter

			# update found to True

	# return found
	return found
