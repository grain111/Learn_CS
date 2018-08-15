import heapq

def DJ(graph, snode):
    visited = []
    parent = {snode: None}
    N = {snode: 0}
    next = [[N[snode], snode]]

    while next:
        node = heapq.heappop(next)
        visited.append(node[1])
        N[node[1]] = node[0]

        for n, w in graph[node[1]]:
            if (n not in N) or (N[n] > N[node[1]] + w):
                N[n] = N[node[1]] + w
                parent[n] = node[1]
            if n not in visited:
                present = False
                for i, item in enumerate(next):
                    if item[1] == n:
                        next[i][0] = N[item[1]]
                        heapq.heapify(next)
                        present = True
                        break
                if not present:
                    heapq.heappush(next, [N[n], n])
    return N, parent
