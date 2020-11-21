with open('resources/coordinate.txt', 'r') as file:
    counter = 0
    content = file.read()
    words = content.split()
    for word in words:
        if word[0].isupper():
            counter += 1

print(f"Number of capitalized words: {counter}")
