"""
Day 5 of learning
"""

A_TUPLE = ("Hi", "This","Is","My","Tuple",33,'Hi','again')
B_TUPLE = 23, 44, 'this', 'also','tuple'

print(A_TUPLE)
print(B_TUPLE)

C_TUPLE = [3,2,5], 'here', 22, {
    'key':'value',
    'another_key':'another_value'
}
print(C_TUPLE)
print(C_TUPLE[3]['key'])

print(A_TUPLE.index("This"))
print(A_TUPLE.count('Hi'))
print(A_TUPLE + B_TUPLE)

UNPACKING, A_TUPE, CAN, BE, DONE, LIKE, THIS, SOMEHOW = A_TUPLE

print(UNPACKING)
print(A_TUPE)

VAL1, VAL2 = 22, 24
print(VAL1)

A_DICTIONARY = {'b':1, 'a':10, 'c':22}

# print(list(A_DICTIONARY.items()))
B_DICTIONARY = list(A_DICTIONARY.items())
B_DICTIONARY.sort()
print(B_DICTIONARY)
