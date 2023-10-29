import array

n  = int(input())
mas =  array.array('i', [1 for i in range(n+1)] )
#print(mas)
for i in range(2,n+1):
    for j in range( int(i/2) if i%2==0 else int(i/2)+1 ,i):
        mas[i] += mas[i-j]
    if  i%2==0:
        mas[i]-=1
print(mas[n])

#n  = int(input())

def recurs_lesenki(n:int, m:int):
    if n == 0:
        return 1
    sum = 0
    for i in range(m+1,n+1):
        sum += recurs_lesenki(n-i,i)
    return  sum

print(recurs_lesenki(n,0))







