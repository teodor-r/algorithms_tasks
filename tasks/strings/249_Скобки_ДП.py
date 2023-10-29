s = input()


def answer():
    len_s = len(s)

    mas = [[0]* len_s for i in range(0,len_s)]
    def min_(left,right):
        v2 = 10000
        if left> right:
            return 0
        if s[left] + s[right] in "{}#()#[]":
            v2 =   min_(left+1,right-1)
        temp_min = 10000
        for float_index in range(left,right):
            v = mas[left][float_index] + mas[float_index + 1][right]
            if v < temp_min:
                temp_min = v
        return  min(temp_min,v2) if left!=right else 1


    for i in range(0, len_s):
        mas[i][i] = 1
        if i!= len_s-1:
            if s[i:i+2] in "{}#()#[]":
                mas[i][i+1] = 0
            else:
                mas[i][i + 1] = 2
    if len_s==2:
        print(mas[0][1])
        return
    for i in range(2,len_s):
        for j in range(0,len_s-i):
            mas[j][j + i] = min_(j, j+i)
    print(mas[0][len_s-1])
answer()







