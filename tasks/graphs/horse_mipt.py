from collections import deque
deque = deque()
def  bfs(graph,n,start_vertex,deque,distances,parents):
    distances[start_vertex] = 0
    parents[start_vertex] = start_vertex
    deque.append(start_vertex)
    while deque:
        current_node = deque.popleft()
        for neib in graph[current_node]:
            if  distances[neib] == None:
                deque.append(neib)
                distances[neib] = distances[current_node] +1
                parents[neib] = current_node
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
def generate_graph():
    alpha = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    graph = { (j,i):set() for j in range(1,9) for  i in range(1,9)}

    def try_to_jump(node, index):
        reverse_index = lambda index:  -index +1  # y = -x +1
        for attempt in [-1,1]:
            new_index = node[index] + 2*attempt
            if   1 <= new_index <= 8:
                index_reverse = reverse_index(index)
                for attempt_few in [-1,1]:
                    new_index_reverse = node[index_reverse] + attempt_few
                    if   1 <= new_index_reverse <= 8:
                        if  index ==0:
                            graph[node].add((new_index,new_index_reverse))
                            graph[(new_index,new_index_reverse)].add(node)
                        else:
                            graph[node].add((new_index_reverse,new_index))
                            graph[(new_index_reverse, new_index)].add(node)

    for node in graph:
        try_to_jump(node,0)
        try_to_jump(node, 1)
    convert_point_to_tuple = lambda point: (alpha[point[0]], int(point[1:]))
    point_from, point_to = [ convert_point_to_tuple(point) for point in input().split()]
    distances = { key: None for key in graph.keys()}
    parents = { key: None for key in graph.keys()}

    bfs(graph,64,point_from,deque,distances,parents)
    path = shortest_path_upon_bfs(point_to, point_from,parents)
    print(path)
    print(point_from,point_to)

generate_graph()