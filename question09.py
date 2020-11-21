n = int(input("Enter 'n': "))
current = n - 5
direction = -1
print("Pattern:")
while current != n + 5:
    if current <= 0:
        direction = 1
    print(current, end=', ')
    current += 5 * direction
