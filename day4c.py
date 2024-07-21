"""
Checking if a word is in a file using a dictionary - counting the words
"""
import sys
STATE = True
while STATE is True:
    FILE_NAME = input("What file would you like to open? ") #name of file
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as FILE_HANDLE: #variable to access file
            WHOLE_FILE = FILE_HANDLE.read() #reads file
            FILE_DICTIONARY = {} #empty dictionary to put words in
            FILE_WORDS = WHOLE_FILE.split() #puts words in a list
            for word in FILE_WORDS: #loops over each word in list
                if word not in FILE_DICTIONARY: #checks if word ia already in dictionary
                    FILE_DICTIONARY[word] = 1 #if not add the word as a key w/ value of 1
                else:
                    FILE_DICTIONARY[word] = FILE_DICTIONARY[word] + 1 # if in add 1 to count
            print(FILE_DICTIONARY)
        sys.exit()
    except FileNotFoundError:
        print("File doesn't exist sorreh")
        continue
