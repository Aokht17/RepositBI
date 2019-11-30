
graph = [[1,2], [0], [0], [3], [5], [4]]

visited = [False] * len(graph)
number_comp = []

def dfs(v):
    """
    graph traversal in depth
    """
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            number_comp.append(1)
            dfs(w)
    return number_comp


def c_c(graph, v, n=None):
    """
 calculates the connected components number in a graph
    :param graph: list of connectivity
    :param v: number of the first analyzed vertex of the graph
    :param n: number of vertexes
    :return: int
    """
    if n is None:
        n=len(graph)
    vis = [False] * n
    for i in range(n):
        if not vis[v]:
            q = dfs(i)
    return len(q)

print(c_c(graph, 0))