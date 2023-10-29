
n  = int(input())
sum = 0
for i in range(0,n):
    s  = [int(s) for s in input().split()]
    sum += s.count(1)

print(int(sum/2))