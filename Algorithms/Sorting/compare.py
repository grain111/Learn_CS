import time, random

from Heap_Sort.HSort_2 import h_sort as h_sort_2
from Heap_Sort.HSort import h_sort as h_sort_1
from Insertion_Sort.InsSort import i_sort
from Merge_Sort.MSort import m_sort

if __name__ == '__main__':
    arg = [[random.randint(0,500) for x in range(10**3)] for y in range(10)]

    start = time.time()
    for arr in arg: i_sort(arr)
    end = time.time()
    print("Insertion sort: {}".format(end-start))

    start = time.time()
    for arr in arg: m_sort(arr)
    end = time.time()
    print("Merge sort: {}".format(end-start))

    start = time.time()
    for arr in arg: h_sort_1(arr)
    end = time.time()
    print("Heap sort 1: {}".format(end-start))

    start = time.time()
    for arr in arg: h_sort_2(arr)
    end = time.time()
    print("Heap sort 2: {}".format(end-start))
