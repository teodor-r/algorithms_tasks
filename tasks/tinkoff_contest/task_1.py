n, s = [int(i) for i in  input().split()]
"""
5 13
3 10 300 15 3
3 4
5 10 12
"""
mas_cost = [int(i) for i in input().split()]

def answer(mas_cost, n,s):
    max_ = 0
    for i in range(n):
        if s>=mas_cost[i]:
            max_ = max(mas_cost[i],max_)

    print(max_)

answer(mas_cost,n,s)
