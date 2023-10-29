def kruskal_alg(R):
    Rs = sorted(R, key=lambda x: x[0],reverse=True)
    U = set()
    D = {}
    T = []
    Rs_additional_reversed = []
    for r in Rs:
        if r[1] not in U or r[2] not in U:
            if r[1] not in U and r[2] not in U:
                D[r[1]] = [r[1], r[2]]
                D[r[2]] = D[r[1]]
            else:
                if not D.get(r[1]):
                    D[r[2]].append(r[1])
                    D[r[1]] = D[r[2]]
                else:
                    D[r[1]].append(r[2])
                    D[r[2]] = D[r[1]]

            T.append(r)
            U.add(r[1])
            U.add(r[2])
        else:
            Rs_additional_reversed.append(r)
    for r in Rs_additional_reversed:
        if r[2] not in D[r[1]]:
            T.append(r)
            gr1 = D[r[1]]
            D[r[1]] += D[r[2]]
            D[r[2]] += gr1

    return T
def ans():
    n, m = map(int, input().split())
    graph = []
    max_ = 0
    for _ in range(m):
        v, u, w = map(int, input().split())
        max_ = max(max_, w)
        if u!=v:
            graph.append((w,u,v))
    result = kruskal_alg(graph)
    if len(result) ==0:
        print(max_)
    else:
        result = min(result,key = lambda cort: cort[0])
        print(result[0]-1)

ans()

