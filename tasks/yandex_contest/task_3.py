from functools import  reduce
n,m,q = [int(i) for i in input().split()]

table = { name:[] for name in input().split()}
result_str = [0]*n
for j in range(n):
    row = [int(i) for i in input().split()]
    for  index,key in enumerate(table.keys(),start=0):
        table[key].append(row[index])

orders_to_sort = []
for i in range(q):
    orders_to_sort.append((input().split()))

def  comp(targer, sym, y):
    if sym == ">":
        return  targer < y
    return targer > y

for order in  orders_to_sort:
    index = 0
    for elem in table[order[0]]:
        if result_str[index]!= -1 and  comp(int(order[2]), order[1], elem):
            result_str[index] +=1
        else:
            result_str[index] = -1
        index+=1

result_sum = 0

def sum_in_str(index_str):
    sum = 0
    for  _,v in table.items():
        sum+= v[index_str]
    return  sum
for index, result  in enumerate(result_str,start=0):
    if result == q:
        result_sum += sum_in_str(index)
print(result_sum)


