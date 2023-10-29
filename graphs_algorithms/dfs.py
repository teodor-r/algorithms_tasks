# поиск компонент сильной связности
def dfs(vertex,G, used):
    used.add(vertex)
    for  neib in  G[vertex]:
        if neib not  in used:
            dfs(neib,G,used)

# подсчёт компонент сильной связности
N= 0
used = {}
G = None
for vertex in G:
    if vertex not in used:
        dfs(vertex,G,used)
        N+=1