n = int(input())
l = list(map(int, input().split()))
l_were = [0] * len(l)
if l[0] == -1:
    print("NO")
else:
    cur_team = 0
    l_were[0] = 1
    while True:
        cur_team = l[cur_team]
        if l_were[cur_team] == 1:
            print("YES")
            break
        elif  l[cur_team] ==-1:
            print("NO")
            break
        l_were[cur_team] = 1
