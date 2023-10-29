
def ans():
    n = int(input())
    pref = [0] * n
    a = [int(i) for i in input().split()]
    b = []
    i = 0
    for num  in input().split():
        b.append(int(num))
        if i >=1:
            if b[i - 1] <= b[i] :
                pref[i] = 1
            pref[i] += pref[i - 1]
        i+=1

    left_flag= True
    right_flag = True
    l_i = 0
    r_i = n-1
    #prefix function is better here
    while left_flag ==True or  right_flag ==True:
        if l_i>r_i:
            print("Yes")
            return
        if a[l_i] == b[l_i]:
            l_i+=1
        else:
            left_flag = False
        if a[r_i] == b[r_i]:
            r_i-=1
        else:
            right_flag = False
    if  l_i == r_i:
        print("No")
        return
    else:
        if  pref[r_i] - pref[l_i] == r_i - l_i:
            if  sorted(a[l_i:r_i+1]) == b[l_i:r_i+1]:
                print("Yes")
                return
        print("No")
        return

ans()





