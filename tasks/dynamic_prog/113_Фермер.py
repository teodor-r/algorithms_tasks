n = int(input())

first  = [0]*(n+1)
second  = [0]*(n+1)

# Экономно по памяти, помним только  последние две строки матрицы
max_ = 0
for i in range(1,n+1):
    second = [0] + [int(s) for s in input()]
    for  j in range(1,n+1):
        if second[j] !=0:
            s = first[j-1]
            if first[j]>=s and second[j-1] >= s:
                pass
            else:
                s = min(first[j],second[j-1])
            second[j] = s + 1
            max_ = max(max_, s + 1)
    first = second

print(max_**2)

#Неэкономно по памяти

"""max_ = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if mas[i][j] !=0:
            s = mas[i-1][j-1]
            if mas[i-1][j]>= s and mas[i][j-1]>= s:
                pass
            else:
                s = min(mas[i-1][j],mas[i][j-1])
            mas[i][j] = s + 1
            max_ = max(max_, s + 1)
print(max_**2)
            """





