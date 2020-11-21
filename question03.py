#caesar cipher
def caesar_cipher(plain_text, shift):
    letters = list(plain_text.lower())
    
    for i, letter in enumerate(letters):
        if letter.isalpha():
            letters[i] = chr((ord(letter) - 97 + shift)% 26 + 97)

    return ''.join(letters)

text = input("enter text to be encrypted: ")
shift = int(input("Enter shift value: "))
print(caesar_cipher(text, shift))