"""
Day one of my lessons relearning python basics and beyond
"""

# Variables
StrType = type("hello world!")
QOUTIENT = 7 // 3
REMAINDER = 7 % 3
print("for 7 divided by 3: ")
print("qoutient:", QOUTIENT, "and remainder: ", REMAINDER)

# INPUT
print("Let's add some numbers.")
INP = input(" Pick the first number:")
INP2 = input("Pick the second number: ")

parsedINP = int(INP)
parsedINP2 = int(INP2)

RESULT = parsedINP + parsedINP2

print("The result is: ", RESULT)

# STRING OPERATIONS
# The string is concatenated, meaning pushed together
print("Hello" + " " + "world")

# Types
FLOAT = 3.2
INTEGER = 3
STRING = "'A string '"


print("The type of", FLOAT, "is: ", type(FLOAT))
print("The type of", INTEGER, "is: ", type(INTEGER))
print("The type of", STRING, "is: ", type(STRING))

FLOATPLUSINTEGER = FLOAT + INTEGER
print(
    "When adding the float",
    FLOAT,
    "to the integer",
    INTEGER,
    "the result is",
    FLOATPLUSINTEGER,
)
print("Which is a", type(FLOATPLUSINTEGER))

# Long numbers

print(1, 000, 000)  # invalid
print(1000000)  # valid

# Operators and Operands
print(3 + 2)  # addition
print(3 % 2)  # remainder/modulus
print(4 * 2)  # multiplication
print(4**2)  # exponent
print(4 - 2)  # subtractiond

RANDNUMBA = 18
print(RANDNUMBA + 2)  # adding w/ variables

# Order of operations
# Python follows PEMDAS
# Parenthasis
# Exponent
# multiplication
# Dividsion
# Addition
# Subtraction

# mnemonic naming
WORDCOLLECTION = ""
WORDS = ["hello", "my", "name", "is", "bill"]
for word in WORDS:
    WORDCOLLECTION = WORDCOLLECTION + " " + word
    print(WORDCOLLECTION)
