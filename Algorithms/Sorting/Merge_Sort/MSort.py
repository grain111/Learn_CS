def m_sort(arr):
    if len(arr) == 0: return None
    if len(arr) == 1: return arr

    mid = len(arr) // 2
    return merge(m_sort(arr[:mid]), m_sort(arr[mid:]))

def merge(a, b):
    # print("Merging {} and {}".format(a, b))
    temp = []
    index_a = 0
    index_b = 0

    for i in range(len(a) + len(b)):
        if a[index_a] <= b[index_b]:
            temp.append(a[index_a])
            index_a += 1
            if index_a == len(a):
                temp += b[index_b:]
                break
        elif a[index_a] > b[index_b]:
            temp.append(b[index_b])
            index_b += 1
            if index_b == len(b):
                temp += a[index_a:]
                break
    return temp
