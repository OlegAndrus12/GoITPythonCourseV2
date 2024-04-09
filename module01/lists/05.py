# buble sort, сортування бульбашкою


def bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


l = [1, 3, 2, 5]
print(l)
sorted_list = bubble_sort(l)
print(sorted_list)
