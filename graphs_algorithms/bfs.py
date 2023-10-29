from collections import deque
deque = deque()
"""
>>>7 8
0 1
1 2
1 3
2 4
3 4
3 6
4 5
5 6

{0: {1}, 1: {0, 2, 3}, 2: {1, 4}, 3: {1, 4, 6}, 4: {2, 3, 5}, 5: {4, 6}, 6: {3, 5}} - graph
[None, 0, 1, 1, 2, 4, 3] - parents
[0, 1, 2, 4, 5] - path from 0 to 5
"""

def input_graph():
    n, m = map(int, input().split())
    graph = {i: set() for i in range(n)}
    for i in range(m):
        v, u = map(int, input().split())
        graph[v].add(u)
        graph[u].add(v)
    return  n,m, graph

n,m,graph = input_graph()
print(graph)
def  bfs(graph,n,start_vertex,deque):
    distances = [None] * n
    distances[start_vertex] = 0
    parents = [0] * n
    parents[start_vertex] = start_vertex
    deque.append(start_vertex)
    while deque:
        current_node = deque.popleft()
        for neib in graph[current_node]:
            if  distances[neib] == None:
                deque.append(neib)
                distances[neib] = distances[current_node] +1
                parents[neib] = current_node
    return distances,parents

distances, parents = bfs(graph,n,0,deque)
print(parents)
def shortest_path_upon_bfs(end_vertex,start_vertex,parents):
    path = [end_vertex]
    if end_vertex == start_vertex:
        return path
    parent = parents[end_vertex]
    while  parent != parents[parent]:
        path.append(parent)
        parent = parents[parent]
    path.append(start_vertex)
    return  path[::-1]
print(shortest_path_upon_bfs(3,0,parents))





