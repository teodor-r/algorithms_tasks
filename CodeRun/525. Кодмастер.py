import sys
import math as m


def find_max_k():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    a = list(filter(lambda x: x != 0, a))  # iterat
    #print(a)
    ans  =  0
    k_max = 0
    for i in range(len(a)):
        k = m.floor(a[i])
        if i+1>=k:
            k_max = max(k_max, k)
            break
        else:
            k_max = max(k_max, i+1)
    print(k_max)

find_max_k()
