def push(array, item):
    array.append(item)


def pop(array):
    try:
        if len(array) > 0:
            return array.pop()
    except OverflowError:
        return


stack = []
with open('resources/coordinate.txt', 'r') as file:
    for line in file:
        push(stack, line.strip())

for _ in range(len(stack)):
    print(pop(stack), '\n')
