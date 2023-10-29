import time
def find_connected_groups(graph):
    n = len(graph)
    visited = [False] * n
    groups = []

    for node in range(n):
        if not visited[node]:
            group = []
            dfs(node, group, visited, graph)
            groups.append(group)

    return groups


def remove_edges(graph, x):
    new_graph = [[] for _ in range(len(graph))]

    for node, neighbors in enumerate(graph):
        for neighbor, weight in neighbors:
            if weight > x:
                new_graph[node].append((neighbor, weight))

    return new_graph


def dfs(node, component, visited, graph):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor[0]]:
            dfs(neighbor[0], component, visited, graph)

start_time  = 0.0
def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    set_weights = []
    for _ in range(m):
        v, u, w = map(int, input().split())
        graph[v - 1].append((u - 1, w))
        graph[u - 1].append((v - 1, w))

        set_weights.append(w)
    global  start_time
    start_time = time.time()
    set_weights = set(set_weights)

    connected_groups = find_connected_groups(graph)
    number_of_groups = len(connected_groups)

    for x in set_weights:
        new_graph = remove_edges(graph, x)

        connected_groups = find_connected_groups(new_graph)
        if len(connected_groups) != number_of_groups:
            print(x - 1)
            break


if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))