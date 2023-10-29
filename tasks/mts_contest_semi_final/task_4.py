n = int(input())

ans = lambda x: x**2/4 if x%2==0 else x -1

print(ans(n)%998244353)