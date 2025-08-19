"""
Day 4 of relearning python
"""
import string

KEVIN_INFO = {
    'name': 'Kevin',
    'age': 25,
    'birthday': 'January 29, 2002',
    'cat_names': ['Jeremy', 'Star', 'Megan'],
    True: 'yes',
    25: ['still', 'valid', 32]
}

print(KEVIN_INFO['age'])
print(KEVIN_INFO['cat_names'])
print(KEVIN_INFO[True])
print(KEVIN_INFO[25])
print(f'keys: {KEVIN_INFO.keys()}')
print(f'values: {KEVIN_INFO.values()}')
#checking if key is in dictionary
print('name' in KEVIN_INFO)

print(dir(string))
print(string.punctuation)
print(string.ascii_letters)
print(string.whitespace)
print(string.hexdigits)
print(string.ascii_uppercase)
