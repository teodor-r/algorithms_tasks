
def ans():
    str = input()
    a =  [ int(s) for s in str]
    b = [ (0,0,0) for i in range(4)]
    for i in range(1,4):
        if a[i]-1 == a[i-1]:
            b[i] = (i,b[i-1][1],i)
        elif a[i]+1 == a[i-1]:
            b[i] = (b[i - 1][0], i,i)
        elif a[i] == a[i-1]:
            b[i]= (i,i,b[i - 1][2])
        else:
            b[i] = (i, i, i)
    print(b)
    def vars(x):
        if 0<x <=7:
            return 1
        elif x>7:
            return x - 7 +1
        return 0
    choice =  min(b[-1])
    if  b[-1][0] == b[-1][1] == b[-1][2]:
        ans  = 1
        if a[3] >=7:
            ans += vars(a[3])
        elif 9-a[3] >=7:
            ans+= vars(9-a[3])
        print(ans)
        return
    if  b[-1][0]  == choice:
        row =  3 - b[-1][0] +1
        vars_1  = vars(a[3])
        vars_2  = vars(9 - a[3])
        if  row + a[3] > 9 - a[3]:
            print(vars_1)
            return
        elif row + a[3] < 9 - a[3]:
            print(vars_2)
            return
        else:
            print(vars_1+vars_2)
            return
        #descending
    elif b[-1][1] == choice:
        row = 3 - b[-1][1] + 1
        vars_1 = vars(9 - a[3])
        vars_2 = vars(a[3])
        if row + 9 - a[3] > a[3]:
            print(vars_1)
            return
        elif row + 9 - a[3] < a[3]:
            print(vars_2)
            return
        else:
            print(vars_1 + vars_2)
        #ascnedning
    else:
        print(1)
        #qeal
ans()