"""
Day 3 of learning python
"""
COUNT = 0
with open('random.md', 'r', encoding='utf-8') as RANDOM_FILE:
    for line in RANDOM_FILE:
        print(line)
        COUNT+= 1
        print(COUNT, "lines so far")

print(f"There are {COUNT} lines total")

#with open("random.md","a+",encoding="utf-8") as FILE_TO_APPEND:
 #   FILE_TO_APPEND.write("\n There be dragons \n")
  #  for line in FILE_TO_APPEND:
   #     print(line)
LINE_COUNT = 0
with open('random.md','r',encoding='utf-8') as file_handle:
    # printing the entire file:
    # print(file_handle.read())
    # searching for a specific line:
    for line in file_handle:
        LINE_COUNT+= 1
        if "There be dragons" in line.strip():
            print(f" Line #{LINE_COUNT} includes: {line}".rstrip())


# Use the file name mbox-short.txt as the file name
file_name = input("Enter name of file:")
spam_confidence_count = 0
line_count = 0
with open(file_name.strip(),'r',encoding='utf-8') as file_handle:
    for line in file_handle:
        if 'X-DSPAM-Confidence' in line:
            spam_confidence_on_line = line[line.rindex(':')+ 1:]
            print(spam_confidence_on_line)
            spam_confidence_count += float(spam_confidence_on_line)
            line_count += 1
            print(line_count)

print(f"Average spam confidence: {spam_confidence_count/line_count}")
