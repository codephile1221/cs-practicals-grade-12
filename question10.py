N = int(input("Enter N: "))


def print_multiplication(N, multiplier=1):
    print(f"{N} * {multiplier} = {N * multiplier}")
    if multiplier == 10:
        return multiplier - 1
    return print_multiplication(N, multiplier + 1)


print_multiplication(N)
