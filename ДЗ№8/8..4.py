graph = [[1, 2, 3], [0], [0], [0,3], [5], [4]]


def dfs(graph, v, visited):
    """
    graph traversal in depth
    """
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)


def c_c(graph, v):
    """
 calculates the connected components number in a graph
    :param graph: list of connectivity
    :param v: number of the first analyzed vertex of the graph
    :return: int
    """
    visited = [False] * len(graph)
    dfs(graph, v, visited)
    comp_c = 1
    for i in range(len(graph)):
        if not visited[i]:
            comp_c += 1
            dfs(graph, i, visited)
    return comp_c


print(c_c(graph,0))