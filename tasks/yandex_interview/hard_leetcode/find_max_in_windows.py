from collections import  deque

def solution():
    global  deque
    deque = deque()
    arr = [5,4,2,3,1,0,-6]
    deque.add(min(arr[0:2]))
    deque.add(max(arr[0:2]))
    ans  = []
    k= 3
    for i in range(len(arr)-k-1):
        target_index = i+2
        max_elem = deque.pop()
        if arr[target_index] > max_elem:
            deque.add(arr[target_index])

