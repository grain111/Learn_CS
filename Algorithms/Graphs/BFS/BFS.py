def BFS(v, adj):
    level = {v: 0}
    parent = {v: None}
    i = 1
    frontier = [v]

    while frontier:
        next = []
        for vertex in frontier:
            for n in adj[vertex]:
                if n not in level:
                    level[n] = i
                    parent[n] = vertex
                    next.append(n)
        frontier = next
        i += 1

    return level, parent
