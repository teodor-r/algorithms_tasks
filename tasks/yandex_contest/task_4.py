from collections import deque
s = deque()

class Node():
    def  __init__(self):
        self.parent = 0
        self.childs = []


def construct_graph(list,graph):
    s.append(0)
    prev_elem_in_deq = 0
    for elem in list[1:]:
        if elem==prev_elem_in_deq:
            _ = s.popleft()
            parent = s.popleft()
            graph[parent][0].add(elem)
            graph[elem][0].add(parent)
            s.appendleft(parent)
        else:
            s.append(elem)
            prev_elem_in_deq = elem
def ans():
    n = int(input()) +1
    graph = { i:(set(),set(),0) for  i in range(n)}
    graph[0][1].add("A")
    graph[0][1].add("B")
    for index, lang in   enumerate(input().split(),start=1):
        graph[index][1].add(lang)

    construct_graph([int(i) for i in input().split()],graph)
    print(graph)


ans()

