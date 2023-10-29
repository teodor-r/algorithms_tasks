import  numpy as np


def gcd (a:int,b:int) -> int:
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)

def ans():
    n = int(input())
    ans = [ ]
    for  i in range(n):
        str = input().split(".")
        if len(str) == 1:
            ans.append([str[0],1])
            continue
        else:
            a = int(str[0])
            b = int(str[1]) if int(str[1]) >=10 else int(str[1]) *10
            res = a+ b/100
        p  = None
        min_q = 100000000
        for ost in range(b*10,b*10+10):
            gcd_ = gcd(1000, ost)
            p_new = a*1000/gcd_ + b*10/gcd_
            q_new = 1000/gcd_
            if  ((p_new/ q_new) -  res) < 0.1 and  q_new< min_q:
                #print("-----------","p_new", p_new, "q_new", q_new)
                min_q = q_new
                p = p_new
        ans.append((int(p), int(min_q)))
    for i in range(n):
        print(*ans[i])

ans()