"""
Day 4 of relearning python - Sorting unique values in a file
"""

# sorting unique words in order
#open : 'romeo.txt'
START = True
while START is True:
    FILE_NAME = input("Which file would you like to open?\n")
    try:
        with open(FILE_NAME.strip(), 'r', encoding="utf-8") as FILE_HANDLE:
            FULL_FILE = FILE_HANDLE.read().split()
            UNSORTED_WORDS = []
            for WORD in FULL_FILE:
                if WORD not in UNSORTED_WORDS:
                    UNSORTED_WORDS.append(WORD.lower())
            SORTED_WORDS = UNSORTED_WORDS[:]
            SORTED_WORDS.sort()
            print("Unsorted:")
            print(UNSORTED_WORDS)
            print("Sorted:")
            print(SORTED_WORDS)
        START = False
    except TypeError :
        print('File not named after a number sorreh. Try again')
        continue
    except FileNotFoundError:
        print('Wrong file. Please try another one')
        continue



