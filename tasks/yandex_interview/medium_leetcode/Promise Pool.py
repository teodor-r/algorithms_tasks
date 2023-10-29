from collections import  deque
def solution():
    arr = [300,400,300,100,200]
    n = 2
    deq = deque(arr)
    deq_executing = deque()
    t_e = []
    current_time = 0
    while deq:
        for i in range(n):
            w_t = arr.popleft()
            t_e.append(current_time+w_t)
