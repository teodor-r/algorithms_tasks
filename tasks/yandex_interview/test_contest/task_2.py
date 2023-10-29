
n = int(input())

max_subsq = 0
counter = 0
for i in range(n):
    bit = int(input())
    if bit==1:
        counter+=1
        max_subsq = max(max_subsq,counter)
    else:
        counter= 0
print(max_subsq)

