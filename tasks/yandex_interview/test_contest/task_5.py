
str1 = input()
str2 = input()


dict  = {}
sum  = 0
def ans():
    if len(str1) != len(str2):
        print(0)
        return
    for i in range(len(str1)):
        if dict.get(str1[i]):
            dict[str1[i]][0]+=1
        else:
            dict[str1[i]]=[1,0]
        if dict.get(str2[i]):
            dict[str2[i]][1]+=1
        else:
            dict[str2[i]]=[0,1]


    if  len(list(filter(lambda key: dict[key][1] - dict[key][0]  , dict)))!=0:
        print(0)
    else:
        print(1)
ans()
