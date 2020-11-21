def redact_text(text, redacted_word):
    return text.replace(redacted_word, 'REDACTED')
    

text = input("enter text:")
word = input('enter word to be readacted: ')
print(redact_text(text, word))