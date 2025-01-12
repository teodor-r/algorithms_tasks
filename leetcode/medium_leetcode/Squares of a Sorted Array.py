import math as m
def solution():
    arr = [-10, 1,2,3,7,8]
    first_positive_index = None
    ans  = []
    for i in range(1,len(arr)):
        if  arr[i] * arr[0] <=0:
            first_positive_index = i
            break
    if first_positive_index == None:
        print(*map(lambda x:x**2,arr))
    else:
        left_index = first_positive_index-1
        right_index = first_positive_index
        print(left_index,right_index)
        while  left_index!= -1 and right_index!=len(arr):
            if m.fabs(arr[left_index]) > arr[right_index]:
                ans.append(arr[right_index]**2)
                right_index+=1
            else:
                ans.append(arr[left_index] ** 2)
                left_index -= 1
        if left_index == -1:
            ans +=  map(lambda x:x**2, arr[right_index:len(arr)])
        else:
            ans += reversed(list(map(lambda x:x**2, arr[0:left_index+1])))
        print(ans)
solution()

