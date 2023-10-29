from collections import deque
deque = deque()
# [-5,-4,-3,0,1,4,6]
#[9,16,25] [0,1,9,16] [16,25]
def input_graph():
    n = int(input())
    graph = {}
    for i in range(n):
        v, u = map(int, input().split())
        if graph.get(v)!=None:
            graph[v].add(u)
        else:
            graph[v] = {u}
        if graph.get(u)!=None:
            graph[u].add(v)
        else:
            graph[u] = {v}
    k = int(input())
    source_p,dest_p = map(int, input().split())
    return  n, graph,k, source_p,dest_p

n, graph,k, source_p,dest_p = input_graph()
print(graph)
def  bfs(graph,n,start_vertex,deque):
    distances = {key: None for key in graph.keys()}
    distances[start_vertex] = 0
    parents = {key: 0 for key in graph.keys()}
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

distances, parents = bfs(graph,n,source_p,deque)
print(distances)

