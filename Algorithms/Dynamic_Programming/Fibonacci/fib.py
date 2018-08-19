def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

memo = {}
def fib_v2(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        memo[n] = fib_v2(n-1) + fib_v2(n-2)
        return memo[n]

def fib_v3(n):
    Q = []
    for i in range(n + 1):
        if i == 0:
            Q.append(0)
        elif i == 1 or i == 2:
            Q.append(1)
        else:
            Q.append(Q[i-1] + Q[i-2])
    return Q[n]

def fib_v4(n):
    Q = []
    for i in range(n + 1):
        if i == 0:
            Q.append(0)
        elif i == 1 or i == 2:
            Q.append(1)
        else:
            Q.append(Q[i-1] + Q[i-2])
            if len(Q) == 3:
                Q = Q[1:]
    return Q[-1]

def fib_v5(n):
    Q = {}
    for i in range(n + 1):
        if i == 0:
            Q[i] = 0
        elif i == 1 or i == 2:
            Q[i] = 1
        else:
            Q[i] = Q[i-1] + Q[i-2]
    return Q[n]

if __name__ == "__main__":

    import time, random

    set = [random.randint(10, 32) for x in range(10**1)]
    st = time.time()
    for s in set:
        fib(s)
    et = time.time()
    print("Naive implementation, set1: {}".format(et-st))

    st = time.time()
    for s in set:
        fib_v2(s)
    et = time.time()
    print("DP implementation, set1: {}".format(et-st))

    print("\n")

    set = [random.randint(500, 1000) for x in range(10**3)]
    st = time.time()
    for s in set:
        fib_v2(s)
    et = time.time()
    print("DP memo implementation, set2: {}".format(et-st))

    st = time.time()
    for s in set:
        fib_v3(s)
    et = time.time()
    print("DP Bottom-Up implementation, set2: {}".format(et-st))

    st = time.time()
    for s in set:
        fib_v5(s)
    et = time.time()
    print("DP Bottom-Up implementation with dict, set2: {}".format(et-st))

    st = time.time()
    for s in set:
        fib_v4(s)
    et = time.time()
    print("DP Bottom-Up SE implementation, set2: {}".format(et-st))
