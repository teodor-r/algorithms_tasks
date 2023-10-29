dict = {
    'a':1,
    'b': 2131,
    'c': 112321,
    'd': 12,
}

dict.update({"key":2})
max_1 = (0,0)
max_2 = (0,0)
lst = list(dict.items())
for item in lst:
    max_1 = max( item ,max_1, key = lambda tpl:tpl[1])
    if max_1!= item:
        max_2= max( item ,max_2, key = lambda tpl:tpl[1])

print(max_2)


sorted_ = sorted(dict.items(),key= lambda x:x[1])
print(sorted_[-2][0])
print(sorted_)