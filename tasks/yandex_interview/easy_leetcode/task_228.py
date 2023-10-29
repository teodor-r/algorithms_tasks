"""Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
def solution():
    ans  = []
    arr = [1,2,3,4,0]
    start_index_seq = 0
    for i in range(1,len(arr)):
        if arr[i]-1 != arr[i-1]:
            if  start_index_seq == i-1:
                ans.append(f"{arr[start_index_seq]}")
            else:
                ans.append(f"{arr[start_index_seq]}->{arr[i]}")
            start_index_seq = i
        if i == len(arr) -1:
            if start_index_seq == i:
                ans.append(f"{arr[start_index_seq]}")
            else:
                ans.append(f"{arr[start_index_seq]}->{arr[len(arr) -1]}")

    print(ans)
solution()

