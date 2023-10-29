from collections import deque
s = deque()
"""
Обратная польска нотация

(2+7) * 5 = [2,7+5*]
2+7*5 = [2,7,5 * +]
В стек будем класть только числа
"""

def reverse_polish_record(A:list):
    operations = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
    }
    for  i in A:
        if type(i) is int:
            s.append(i)
        else:
            assert  i in "*/+-", "Неверная нотация"
            x = s.pop()
            y = s.pop()
            s.append(operations[i](y,x))
    return s.pop()

print(reverse_polish_record([2,7,"*",5,"*"]))




