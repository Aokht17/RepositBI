
graph = [[1,2], [0], [0], [3], [5], [4]]

visited = [False] * len(graph)
number_comp = []

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            number_comp.append(1)
            dfs(w)
    return number_comp


def c_c(graph, v, n=None):
    if n is None:
        n=len(graph)
    vis = [False] * n
    for i in range(n):
        if not vis[v]:
            q = dfs(i)
    return len(q)

print(c_c(graph, 0))