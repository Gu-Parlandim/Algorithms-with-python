# 4.1
def list_sum(arr: list, current_row: int):
    if (len(arr) == 1):
        return arr[current_row]
    if (len(arr) == 0):
        return 0
    if (len(arr) == current_row):
        return 0
    return arr[current_row] + sum(arr, current_row + 1)

# 4.2


def count(arr: list, current_row):
    if (not arr[current_row]):
        return 0
    return 1 + count(arr, current_row + 1)
