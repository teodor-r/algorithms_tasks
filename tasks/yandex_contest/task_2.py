import  math as mathh
from collections import deque
n,m,q = [int(i) for i in input().split()]
ans_list = []
dict_rest_cards = {}
sum = 0
for  elem in  input().split():
    num = int(elem)
    if dict_rest_cards.get(num) != None:
        dict_rest_cards[num] +=1
    else:
        dict_rest_cards[num] = 1
    sum+=1
for  elem in  input().split():
    num = int(elem)
    if dict_rest_cards.get(num) != None:
        dict_rest_cards[num] -=1
        #dict_rest_cards[num]= mathh.fabs(dict_rest_cards[num])
        if  dict_rest_cards[num]>=0:
            sum -= 1
        else:
            sum +=1
    else:
        dict_rest_cards[num] = -1
        sum+=1
#print(dict_rest_cards)


def compute_mng(player, card):
    diff = 0
    if  dict_rest_cards.get(card)!=None:
        if dict_rest_cards[card] * player <0:
            diff = -1
        else:
            diff = 1
        dict_rest_cards[card] = dict_rest_cards[card] + player
    else:
        dict_rest_cards[card] = player
        diff = 1
    return  diff



for  i in range(q):
    type, player, card = input().split()
    player  =  1 if  str(player) == 'A' else -1
    type = int(type)
    card = int(card)
    if type == -1:
        sum += compute_mng(-1 * player, card)
    else:
        sum += compute_mng(player, card)
    ans_list.append(sum)

print(*ans_list)




