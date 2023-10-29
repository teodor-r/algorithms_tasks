from functools import reduce
n = int(input())

dict_relations = {1:[6,8],
                  2:[7,9],
                  3:[4,8],
                  4:[0,3,9],
                  5:[],
                  6:[0,1,7],
                  7:[2,6],
                  8:[1,3],
                  9:[2,4],
                  0:[4,6]}
dm = [[0]*10 for i in range(n+1)]
dm[1] = [1,1,1,1,1,1,1,1,1,1]
def func(i,j):
    sum = 0
    for  elem in dict_relations[j]:
        sum+= dm[i][elem]
    return sum
    #return reduce(lambda x,y: dm[i][x] + dm[i][y] ,dict_relations[j])

if n>=2:
    dm[2] = [2,2,2,2,3,0,3,2,2,2]
    for  i in range(3,n+1):
        for j in  range(10):
            dm[i][j] += func(i-1,j)
sum=0
for i in range(10):
    if i!= 8 and i!=0:
        sum+=dm[n][i]
print(sum)