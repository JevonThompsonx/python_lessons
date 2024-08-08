"""
final day of regex probably
"""

import re
with open('regexSum2.txt','r',encoding='utf-8') as FILE_HANDLE:
    FILE_READ = FILE_HANDLE.read()
    FULL_LIST = []
    MATCHED_NUMBERS = re.findall(r'\d+',FILE_READ)
    for MATCHED_NUMBER in MATCHED_NUMBERS:
        FULL_LIST.append(int(MATCHED_NUMBER))
    print(sum(FULL_LIST))
