'''Write a function definition for ​JTOI() ​in python that would display the
corrected version of entire content of the file ​WORDS.TXT ​with all the
alphabets “J” to be displayed as an alphabet “I” on screen.
'''


def JtoI(file):
    with open(file, 'r') as words_file:
        content = words_file.read()
        print(content.replace('J', 'I'))


JtoI(file='resources/words.txt')
