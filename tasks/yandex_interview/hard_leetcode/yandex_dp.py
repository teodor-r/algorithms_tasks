
n = int(input())
a = list(map(int,input().split()))
b = [ (0,0,0) for i in range(n)]

for i in range(1,n):
    if a[i]-1 == a[i-1]:
        b[i] = (i,b[i-1][1],i)
    elif a[i]+1 == a[i-1]:
        b[i] = (b[i - 1][0], i,i)
    elif a[i] == a[i-1]:
        b[i]= (i,i,b[i - 1][2])
    else:
        print(i)
        b[i] = (i,i,i)


print( min(b[-1]))
max_ = 0
print(b)
for i  in range(n):
    max_l = max(i - b[i][0],i- b[i][1] )
    max_ = i if max_l > max_ else max_

print(min(b[max_][0],b[max_][1] ),max_)



