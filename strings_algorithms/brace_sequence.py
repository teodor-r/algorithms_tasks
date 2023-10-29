from collections import deque
s = deque()
# примечание deque- двустороння очередь, можно вытаскивать за O(1) с обоих концов
# В данном случае работаем как со стеком
def  is_brace_sequence_correct(A:str):
    answer = lambda x: True if x ==0 else False
    for brace in A:
        if brace in "([":
            s.append(brace)
        else:
            if len(s) ==0:
                return False
            else:
                left_brace = s.pop()
                if left_brace == "(":
                    right_brace = ")"
                else:
                    right_brace = "]"
                if brace != right_brace:
                    return False
    return answer(len(s))

print(is_brace_sequence_correct("()()()[]"))
