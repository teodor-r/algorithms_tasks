a, b = [int(s) for s in input().split()]

def gcd (a:int,b:int) -> int:
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)
#lambda_ =  lambda a,b: a*b/ gcd(a,b) if a!=0 and b!=0 else max(a,b)
print(a*b/ gcd(a,b))

