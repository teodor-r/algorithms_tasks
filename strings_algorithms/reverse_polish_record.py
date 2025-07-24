from collections import deque
s = deque()

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




