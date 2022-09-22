def binary_search(list: list[int], item: int):
    low = 0
    high = len(list) - 1  # array length
    while low <= high:
        middle = int((low + high) / 2)
        shot = list[middle]

        if (shot == item):
            return middle  # return item indice
        if (shot > item):
            high = middle - 1  # update max value
        else:
            low = middle + 1
    return None


my_array = [5, 10, 15, 20, 25, 41, 43, 44, 50, 60, 80]


print(binary_search(my_array, 5))
