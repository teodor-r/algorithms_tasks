
d = {}
def delit(a):
    g= 0
    i = 2
    while i * i < a + 1:
        if a % i == 0:
            d[i] = 1
            a //= i
            while a % i == 0:
                d[i] += 1
                a //= i
        i += 1
    if a != 1:
        d[a] = 1
    #return d

a = int(input())
delit(a)
num_euiler = 1
for  k,v in d.items():
    num_euiler*= k**v - k**(v-1)
print(num_euiler)