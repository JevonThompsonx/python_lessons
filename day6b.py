"""
Day 6b of relearning & learning python -
Tuple counting
"""
import string
# The goal is to take a file and count the repeating words
#then organizing by which word repeats the most

with open(input("Which file should we use for the count? "), 'r', encoding='utf-8') as FILE_HANDLE:
    READ_FILE = FILE_HANDLE.read()
    READ_FILE.translate(str.maketrans('', '', string.punctuation))
    # bc 3 param is optional, all params needed ^
    WORDS_IN_FILE_SPLIT = READ_FILE.split()
    #print(WORDS_IN_FILE_SPLIT)
    COUNTING_DICTIONARY = {}
    for word in WORDS_IN_FILE_SPLIT:
        if word in COUNTING_DICTIONARY:
            COUNTING_DICTIONARY[word] += 1
        else:
            COUNTING_DICTIONARY[word] = 1
    #print(COUNTING_DICTIONARY)
    COUNTING_UNSORTED_LIST = COUNTING_DICTIONARY.items()
    #print(COUNTING_UNSORTED_LIST)
    COUNTING_LIST_TO_SORT = []
    for word,count in COUNTING_UNSORTED_LIST:
        COUNTING_LIST_TO_SORT.append(tuple((count,word)))
    #print(COUNTING_LIST_TO_SORT)
    COUNTING_LIST_SORTED = COUNTING_LIST_TO_SORT #not sorted here - just copied
    COUNTING_LIST_SORTED.sort(reverse=True) #highest to lowest
    # works bc the left most value in tuple is counted first in sort
    print(COUNTING_LIST_SORTED)
