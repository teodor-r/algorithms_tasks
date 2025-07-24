N,K,T = list(map(int, input().split()))
P = float(input())


def sum():
    res = 0

    if N>K:
        if P == 0:
            print(K*T)
            return
        elif P==1:
            print(0)
            return
        for  j in range(K+1):
            res+= j * ((1-P)**(N-K+j)) *  P**(K-j)
        print(res*T)
    elif N>K:
        for j in range(N+1):
            res += (K-N +j) * ((1 - P) **j) * P**(N - j)
        print(res*T)
    else:
        if  P==0:
            print(K*T)
        elif P==1:
            print(0)
        else:
            for j in range(N + 1):
                res += j * ((1 - P) ** j) * P**(N - j)
            print(res*(T-1))
sum()
