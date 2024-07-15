"""
Day 2 of relearning python basics and going beyond

pairs w/ notes at : https://www.notion.so/jthompsonx/Python-b23bb5e2929c4c8c8be73588a155e595?pvs=4
"""

import math
import random
# Conditionals
# if statements are indended:
    #like so
RANDNUMBER = 35
if RANDNUMBER == 25: # == is used for comparison
    print('The default if statement - Number is 25')
elif RANDNUMBER == 27:
    print('According to the elif - Number is 27')
else:
    print('Random number is', RANDNUMBER)


# try && except
PAYCHECK_CALC_STATE = True
while PAYCHECK_CALC_STATE is True :
    print("Let's calculate pay before taxes")
    USERHOURLY = input("Please input hourly pay: ")
    USERHOURS = input("Please input hours worked: ")
    if USERHOURLY.lower() == 'skip' or USERHOURS.lower() == 'skip':
        break
    try:
        PAY_BEFORE_TAX = int(USERHOURLY) * int(USERHOURS)
        print('Your pay before tax is:', PAY_BEFORE_TAX)
        PAYCHECK_CALC_STATE = False
    except TypeError:
        print('Possible type error')
        continue
# min & max
A_LIST = [24, 43, 23, 100]
print("Here is a list:", A_LIST)
print("The highest number in this list is:",max(A_LIST), "The lowest number is", min(A_LIST))


print(math.pi) # contains pi
print(math.floor(math.sqrt(16))) # uses importated math funcs to floor and find square root of 16

print("Random choice from list:" , random.choice(A_LIST))
print("2 random choices from a list:", random.sample(A_LIST, 2))
print("Random shuffle of the list:", random.shuffle(A_LIST) )
print("A random float between 0.0 and 1.0:", random.random())
print("A random integer between 0 and 10:", random.randint(0,10))

def say_hello():
    """
    Just says hello
    """
    print('Hi there')

say_hello()

def say_hello_with_name(name="Jevon"):
    "says hello to provided name"
    print("Helo there", str(name))

say_hello_with_name("Jacob")
say_hello_with_name()

def addition_function(val_1,val_2):
    """
    Adds 2 nums
    """
    return val_1 + val_2

print(addition_function(2,4))

#Using for...in loops
COUNT = 0
for iterVar in [3, 41, 12, 9, 74, 15]:
    COUNT = COUNT+ 1
    print('COUNT: ', COUNT)

TOTAL = 0
print("Beginning total:",TOTAL)
for iterVar in [3, 243, 32, 93]:
    TOTAL += iterVar
    print('Total:', TOTAL)

#find max
LARGEST_LIST = [12,2,40,33,50, 20, 23, 34, 50]
LARGEST_TRACKER = 0
for list_item in LARGEST_LIST:
    LARGEST_TRACKER = max(LARGEST_TRACKER, list_item)
    print("Current largest value:", LARGEST_TRACKER)

print("Hello world".replace("world","person")) #string method - replacing values

#f string

print(f'Please remeber that the largest value is {LARGEST_TRACKER}')
