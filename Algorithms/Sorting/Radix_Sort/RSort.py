from math import log, floor

def r_sort(arr, base=10):
    d = floor(log(max(arr) + 1, base)) + 1
    for i in range(d):
        arr = c_sort(arr, base - 1, lambda x: (x // base ** i) % base)
    return arr

def c_sort(arr, n, key):
    buckets = [[] for x in range(n + 1)]
    for item in arr:
        buckets[key(item)].append(item)
    ans = []
    for bucket in buckets:
        ans.extend(bucket)
    return ans
