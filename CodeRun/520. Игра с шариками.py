from math import gcd

"""
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
"""
n = int(input())
#print(gcd(126,392))

def sum(a,b,c,d):
    return  a*d + b*c, b*d


res_a,res_b = 0,1

last_pref = [1,1]

for i in range(n):
    arg_3 = 12 * last_pref[0]
    arg_4 =  (2+i)*(3+i)*(7+i) * last_pref[1]

    res_a, res_b = res_a* arg_4 + res_b*arg_3,  res_b*arg_4
    pk_inv1, pk_inv2 = (2 + i) * (3 + i) * (7 + i) - 12, (2 + i)*(3 + i) * (7 + i)

    comm_del = gcd(pk_inv1, pk_inv2)
    pk_inv1, pk_inv2 = int(pk_inv1/comm_del) , int(pk_inv2/comm_del)
    last_pref[0] = last_pref[0]* pk_inv1
    last_pref[1] = last_pref[1]* pk_inv2
    if  last_pref[0] > 10**6 or  last_pref[1] > 10**6:
        comm_del = gcd(last_pref[0] , last_pref[1])
        last_pref[0], last_pref[1]  = int(last_pref[0]/comm_del), int(last_pref[1]/comm_del)


    if res_a > 10**6 or res_b > 10**6:
        comm_del = gcd(res_a, res_b)
        res_a, res_b = int(res_a/comm_del) , int(res_b/comm_del)


comm_del = gcd(res_a,res_b)
print(int(res_a/comm_del) , int(res_b/comm_del) )





