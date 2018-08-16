def BF(graph, snode):
    N = {snode: 0}
    parent = {snode: None}

    for i in range(len(graph) - 1):
        for v, k in graph.items():
            for nd, w in k:
                if v not in N:
                    continue
                elif (nd not in N) or (N[nd] > N[v] + w):
                    N[nd] = N[v] + w
                    parent[nd] = v

    for v, k in graph.items():
        for nd, w in k:
            if N[nd] == None:
                continue
            elif (N[v] == None) or (N[nd] > N[v] + w):
                N[nd] = None
                parent[nd] = None

    return N, parent
