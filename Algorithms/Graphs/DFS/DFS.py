def DFS(graph):
    parent = {}
    tree_edges = []
    back_edges = []
    forward_edges = []
    cross_edges = []

    for node in graph:
        if node not in parent:
            parent[node] = None
            explore_node(graph,
                         node,
                         parent,
                         tree_edges,
                         back_edges,
                         forward_edges,
                         cross_edges)

    return parent, tree_edges, back_edges, forward_edges, cross_edges

def explore_node(graph, _node, parent, te, be, fe, ce):
    for n in graph[_node]:
        if n not in parent:
            parent[n] = _node
            te.append("{}{}".format(parent[n], n))
            explore_node(graph, n, parent, te, be, fe, ce)

        elif is_in_tree(_node, n, parent):
            be.append("{}{}".format(_node, n))

        elif is_in_tree(n, _node, parent):
            fe.append("{}{}".format(_node, n))

        elif _node == n:
            pass

        else:
            ce.append("{}{}".format(_node, n))

def is_in_tree(start_node, ntbc, parent):
    nd = start_node
    while parent[nd] != None:
        if parent[nd] == ntbc:
            return True
        nd = parent[nd]
