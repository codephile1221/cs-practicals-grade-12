'''
recursive program to implement
binary search in a list of integers
'''


def binary_search(element, array, start=0, end=None):
    if not end:
        end = len(array) - 1

    mid = end // 2
    if array[mid] == element:
        return mid
    elif array[mid] > element:  # element is in the 1st half
        return binary_search(element, array, start, mid)
    elif array[mid] < element:  # element is in the 2nd half
        return binary_search(element, array, mid, end)


array = [1, 3, 5, 7, 9]
x = int(input("Element to be searched: "))
print(f"Element found at index position {binary_search(x, array)}")
