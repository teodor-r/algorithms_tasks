import math as math_mod

def binary_search(list_num, first_index, last_index, to_search):
    if last_index >= first_index:

        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]

        if mid_element[1] == to_search:
            return mid_element

        elif mid_element[1] > to_search:
            new_position = mid_index - 1
            # new last index is the new position
            return binary_search(list_num, first_index, new_position, to_search)

        elif mid_element[1] < to_search:
            new_position = mid_index + 1
            # new first index is the new position
            return binary_search(list_num, new_position, last_index, to_search)
    else:
        return None
def ans():
    n,m = [int(i) for i in input().split()]
    mas = [int(i) for i in input().split()]
    mas.sort()
    power = int(math_mod.pow(2,m))
    #print(power)
    def compute_value(num):
        sum =0
        for  i in range(m):
            if num&(1<<i)>0:
                sum+=mas[i]
        return sum

    def print_answer(num_1, num_2):
        sum=0
        temp_mas  = []
        for i in range(m):
            if num_1 & (1 << i) > 0:
                temp_mas.append(mas[i])
                sum +=1
            if num_2 & (1 << i) > 0:
                sum += 1
                temp_mas.append(mas[i])
        print(sum)
        print(*temp_mas)#, end='')

    states = [(i,compute_value(i)) for i in range(power)]
    states.sort(key = lambda x: x[1])

    for i in states:
        if i[1] != n and i[1]<n:
            element = binary_search(states,0, power-1, n-i[1])
            if element!= None:
                print_answer(i[0], element[0])
                return
        elif i[1] == n:
            print_answer(i[0],0)
            return

    print(-1)
ans()

