def binary_search_k(arr,l_i, r_i):
    mid  = int((l_i + r_i)/2)
    if   arr[mid-1] > arr[mid] and arr[mid+1] > arr[mid]  :
        return mid
    if  arr[mid] < arr[r_i]:
        return   binary_search_k(arr, l_i, mid)
    else:
        return   binary_search_k(arr, mid, r_i)
    return  res
def binary_search(arr,l_i, r_i,target):
    mid = int((l_i + r_i) / 2)
    if   arr[mid]==target :
        return mid
    if  l_i == r_i:
        return  -1
    if  arr[mid] < target:
        return   binary_search(arr, mid+1, r_i,target)
    else:
        return   binary_search(arr, l_i, mid-1,target)

def solution():
    arr = [4,5,6,0,1,2,3]
    target  = 7
    res_index = None
    if  arr[len(arr)-1] < arr[0]:
        k = binary_search_k(arr,0,len(arr)-1)
        if target <arr[0]:
            res_index = binary_search(arr,k, len(arr)-1,target)
        else:
            res_index = binary_search(arr, 0, k,target)
        #print(res_index)
    else:
        res_index = binary_search(arr,0, len(arr)-1)
    print("target",res_index)

solution()