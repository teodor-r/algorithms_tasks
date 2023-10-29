"""
задача похожа  на скобочную последовательность из string_algoritms
"""

from collections import deque
from functools import reduce
import copy
# примечание deque- двустороння очередь, можно вытаскивать за O(1) с обоих концов
# В данном случае работаем как со стеком
s  = deque()
str_ = input()

dict_braces = {
    "(":")",
    ")":"(",
    "[":"]",
    "]":"[",
    "{":"}",
    "}":"{",
}

def  is_brc_seq_cor(A:str,s, index):
    counter = 0
    for i in range(index,len(A)):
        brace = A[i]
        if brace in "([{":
            s.append(brace)
        else:
            if len(s) ==0:
                counter+=1
            else:
                left_brace = s.pop()
                right_brace  = dict_braces[left_brace]
                if brace != right_brace:
                    counter+=1
                    result_common = reduce(lambda x,y: x+y, s) if len(s)!=0 else ""
                    result_1 =  result_common + A[i:]
                    result_2 =  result_common + left_brace + A[i + 1:]
                    count_1 = is_brc_seq_cor(result_1,copy.copy(s),len(result_common))
                    s.append(left_brace)
                    count_2 = is_brc_seq_cor(result_2,copy.copy(s),len(result_common+left_brace))
                    counter += min(count_1,count_2)
                    return counter
    return counter + len(s)

print(is_brc_seq_cor(str_,s,0))
