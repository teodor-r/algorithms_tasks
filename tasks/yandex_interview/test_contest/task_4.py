n = int(input())

ans = []
def constuct_seq(count_opened, rest_opened, rest_closed, current_sub,ans):
    if  rest_opened == 0:
        current_sub = current_sub + ")"*rest_closed
        ans.append("("+current_sub+")")
        return
    if  count_opened ==0:
        constuct_seq(1, rest_opened-1,rest_closed,current_sub + "(",ans)
    else:
        constuct_seq(count_opened+1, rest_opened - 1, rest_closed, current_sub + "(",ans)
        constuct_seq(count_opened -1, rest_opened , rest_closed-1, current_sub + ")",ans)
if n==0:
    print("", end='')
else:
    constuct_seq(1, n-1, n-1, "",ans)
    print(*ans, sep= "\n")