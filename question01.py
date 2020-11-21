def pig_latin_decoder(word):
    if word[-2:] == 'ay':
        return f'{word[-3]}{word[:-3]}'
    return word

word = input("Enter a word in pig latin: ")
print(pig_latin_decoder(word))
