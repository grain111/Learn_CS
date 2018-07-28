from math import log, floor
import time

def h_sort(arr):
    if not arr: return None

    n = len(arr)
    heap_height = floor(log(n, 2)) + 1
    start_ind = 2 ** (heap_height - 1) - 2

    for ind in range(start_ind, -1, -1):
        heapify(arr, ind, n)

    for i in range(n):
        swap(arr, 0, n - 1)
        n -= 1
        heapify(arr, 0, n)

    return arr

def heapify(arr, index, n):
    largest = index
    lc = get_child(index, n, 1)
    rc = get_child(index, n, 2)

    if lc != None and arr[lc] > arr[largest]:
        largest = lc
    if rc != None and arr[rc] > arr[largest]:
        largest = rc

    if largest != index:
        swap(arr, index, largest)
        heapify(arr, largest, n)

def get_parent(index):
    return (index - 1) // 2 if (index - 1) // 2 >= 0 else None

def get_child(index, n, val):
    """left child: val = 1, right child: val = 2"""
    ind = (index) * 2 + val
    return ind if ind < n else None

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
