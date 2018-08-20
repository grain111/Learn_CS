def reverse_graph(g):
    result = {}
    for node in g:
        for nb, w in g[node]:
            if nb not in result:
                result[nb] = [[node, w]]
            else:
                result[nb].append([node, w])
    return result
memo = {}
def SP(graph, snode, enode):
    rev_graph = reverse_graph(graph)
    return d(rev_graph, snode, enode)

def d(g, s, v):
    if v in memo:
        return memo[v]
    elif s == v:
        return 0
    else:
        ans = min([d(g, s, u) + w for u, w in g[v]])
        memo[v] = ans
        return ans
