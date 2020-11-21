# bubble sort

def bubble_sorted(array):
    flag = 0
    for i, element in enumerate(array):
        if i+1 != len(array):
            if element > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag += 1
    if flag != 0:
        return bubble_sorted(array)
    else:
        return array


arr = [3, 7, 2, 9, 5, 0]
print("list to be sorted:", arr)
print("Sorted list:", bubble_sorted(arr))

arr = [5, 3, 7, 1, 0, 8]
print("list to be sorted:", arr)
print("Sorted list:", bubble_sorted(arr))
