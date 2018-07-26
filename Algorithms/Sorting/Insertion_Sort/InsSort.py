def i_sort(arr):
    if not arr: return None

    for key, key_val in enumerate(arr):
        index = key
        while index != 0 and arr[index] < arr[index - 1]:
            arr = swap(arr, index, index - 1)
            index -= 1
    return arr

def swap(arr, i, j):
    temp  = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
