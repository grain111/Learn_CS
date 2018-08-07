def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

    return arr

def rotate_hor(arr):
    arr = swap(arr, 0, 2)
    arr = swap(arr, 1, 3)
    arr = swap(arr, 2, 4)
    arr = swap(arr, 3, 5)
    arr = swap(arr, 4, 6)
    arr = swap(arr, 5, 7)

    arr = swap(arr, 16, 18)
    arr = swap(arr, 18, 19)
    arr = swap(arr, 19, 17)

    return "".join(arr)

def rotate_hor_r(arr):
    arr = swap(arr, 6, 4)
    arr = swap(arr, 7, 5)
    arr = swap(arr, 4, 2)
    arr = swap(arr, 5, 3)
    arr = swap(arr, 2, 0)
    arr = swap(arr, 3, 1)

    arr = swap(arr, 16, 17)
    arr = swap(arr, 17, 19)
    arr = swap(arr, 19, 18)

    return "".join(arr)

def rotate_ver(arr):
    arr = swap(arr, 23, 11)
    arr = swap(arr, 21, 3)
    arr = swap(arr, 11, 19)
    arr = swap(arr, 3, 17)
    arr = swap(arr, 19, 6)
    arr = swap(arr, 17, 14)

    arr = swap(arr, 4, 5)
    arr = swap(arr, 5, 13)
    arr = swap(arr, 13, 12)

    return "".join(arr)

def rotate_ver_r(arr):

    arr = swap(arr, 17, 14)
    arr = swap(arr, 19, 6)
    arr = swap(arr, 3, 17)
    arr = swap(arr, 11, 19)
    arr = swap(arr, 21, 3)
    arr = swap(arr, 23, 11)

    arr = swap(arr, 12, 4)
    arr = swap(arr, 12, 13)
    arr = swap(arr, 5, 13)

    return "".join(arr)

def rotate_rot(arr):

    arr = swap(arr, 18, 9)
    arr = swap(arr, 19, 1)
    arr = swap(arr, 9, 21)
    arr = swap(arr, 1, 20)
    arr = swap(arr, 4, 21)
    arr = swap(arr, 12, 20)

    arr = swap(arr, 2, 10)
    arr = swap(arr, 10, 11)
    arr = swap(arr, 11, 3)

    return "".join(arr)

def rotate_rot_r(arr):

    arr = swap(arr, 18, 4)
    arr = swap(arr, 19, 12)
    arr = swap(arr, 4, 21)
    arr = swap(arr, 12, 20)
    arr = swap(arr, 9, 21)
    arr = swap(arr, 1, 20)

    arr = swap(arr, 2, 3)
    arr = swap(arr, 3, 11)
    arr = swap(arr, 11, 10)

    return "".join(arr)

def get_neighbours(s):
    r1 = rotate_hor(list(s))
    r2 = rotate_hor_r(list(s))
    r3 = rotate_ver(list(s))
    r4 = rotate_ver_r(list(s))
    r5 = rotate_rot(list(s))
    r6 = rotate_rot_r(list(s))


    return [r1, r2, r3, r4, r5, r6]

v = 'ooggrryyooggrryywwwwbbbb'

level = {v: 0}
parent = {v: None}
i = 1
frontier = [v]
prev = 1
while frontier:
    next = []
    for vertex in frontier:
        neighbours = get_neighbours(vertex)
        for n in neighbours:
            if n not in level:
                level[n] = i
                # parent[n] = vertex
                next.append(n)
    frontier = next
    print(i, len(level) - prev)
    prev = len(level)
    i += 1
