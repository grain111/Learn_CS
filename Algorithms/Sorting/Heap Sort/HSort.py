from math import log, floor

def h_sort(arr):
    if not arr: return None

    n = len(arr)
    heap_height = floor(log(n, 2)) + 1

    # Heapify the array
    start_ind = 2 ** (heap_height - 1) - 2
    # print(start_ind)
    for ind in range(start_ind, -1, -1):
        # print("Heapifying at index {}, value {}".format(ind, arr[ind]))
        arr = heapify(arr, ind, n)
    # Sorting
    for i in range(n):
        arr = swap(arr, 0, n - 1)
        n -= 1
        arr = heapify(arr, 0, n)

    return arr


def heapify(arr, index, n):

    flag = True
    while flag:
        arr, flag, next = heapify_node(arr, index, n)
        index = next
    return arr

def heapify_node(arr, index, n):

    children = []
    if get_child(arr, index, n, 1): children.append(get_child(arr, index, n, 1))
    if get_child(arr, index, n, 2): children.append(get_child(arr, index, n, 2))
    # print("Children at index {} are {}".format(index, children))
    if len(children) == 0: return arr, False, None
    max_child = max(children, key = lambda x: arr[x])
    if arr[max_child] > arr[index]: arr = swap(arr, index, max_child)
    return arr, True, max_child

def get_parent(index):
    return (index - 1) // 2 if (index - 1) // 2 >= 0 else None

def get_child(arr, index, n, val):
    """left child: val = 1, right child: val = 2"""
    ind = (index) * 2 + val
    return ind if ind < n else None

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr
