def findSmallest(arr):
    small = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if arr[i] < small:
            small = arr[i]
            small_index = i
    return small_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        small = findSmallest(arr)
        # removes the item at the given index from the list and returns the removed item
        newArr.append(arr.pop(small))
    return newArr


my_array = [5, 2, 1, 10, 22, 100, 6, 17, 21, 3, 55, 4]

print(selection_sort(my_array))
