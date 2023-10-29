from functools import reduce
items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a,b: a if (a > b) else b, items)
all_max

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
list(squared)
[1, 4, 9, 16, 25]

numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))

x = [1, 4, 9, 16, 25]
max(x, key=lambda i: int(i))
print(max(x, key=lambda i: i % 5))

lst = [1, 5, 3, 6, 9, 7]
# пронумеруем список
lst_num = list(enumerate(lst, 0))
# найдем максимум (из второго значения кортежей)
t_max = max(lst_num, key=lambda i : i[1])
# [(0, 1), (1, 5), (2, 3), (3, 6), (4, 9), (5, 7)]