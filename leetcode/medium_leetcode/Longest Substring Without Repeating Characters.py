def solution():
    s = "abcdf"
    temp_set = set()
    ans_tuple = (0,1)
    begin_new_seq = 0
    for i in range(len(s)):
        if s[i] not in temp_set:
            temp_set.add(s[i])
            if i - begin_new_seq> ans_tuple[1] - ans_tuple[0]:
                ans_tuple = begin_new_seq,i+1
        else:
            temp_set.clear()
            begin_new_seq = i
    print(s[ans_tuple[0]:ans_tuple[1]])

solution()
