"""
Regex training
"""

import re
with open('regexEx.txt','r',encoding='utf=8') as FILE_HANDLE:
    FILE_READ = FILE_HANDLE.read()
    prices = re.findall(r"\b\w+:\s\$([0-9.]+)\b",FILE_READ)
    print(prices)
    for price in prices:
        print(float(price))
    print(re.findall(r"\bAddress:\s[a-zA-Z0-9, ]{10,}\b",FILE_READ))
    ERRORS = re.findall(r"(?P<error>\[\w+\])\s(?P<message>[a-zA-Z ]+)\b",FILE_READ)
    for error in ERRORS:
        error_val = error[0]
        message = error[1]
        print(error_val)
        print(message)

    PHONE_NUMBER = re.findall(r"\w+:\s(\+[0-9-]+\b)",FILE_READ)
    print(PHONE_NUMBER)
