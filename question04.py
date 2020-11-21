def time_elapsed(parallel_lists, id, time):
    id_array, out_array = parallel_lists
    for i, element in enumerate(id_array):
        if element == id:
            out = out_array[i]
            return time - out
        elif element == 'ZZZ':
            print('ID not found.')
            
    

ids = ['ABC',  'DFK', 'XYY']
out = [9.55, 10.11, 10.23, 0]
parallel_lists = (ids, out)

id = input("Enter id: ")
current_time = float(input("Enter the current time (HH.MM): "))

print(time_elapsed(parallel_lists, id, current_time))
