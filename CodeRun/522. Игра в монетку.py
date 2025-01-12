p  = 0.9
sum = 0
for i in range(1,26):
    sum += p**(i) *( 1/p -1)
print(sum)
res  = 1 - sum**15
print(res)