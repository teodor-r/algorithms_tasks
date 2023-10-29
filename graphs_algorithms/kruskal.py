#R = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
#         (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6),(20,4,6)]#, (1,7,8), (2,8,9)]
R = [(13,1,1), (14,2,2), (15,4,3), (16,3,4)]
def kruskal_alg(R):
    Rs = sorted(R, key=lambda x: x[0],reverse=True)
    U = set()   # список соединенных вершин
    D = {}      # словарь списка изолированных групп вершин
    T = [] # список ребер остова
    Rs_additional_reversed = []
    for r in Rs:
        if r[1] not in U or r[2] not in U:  # проверка для исключения циклов в остове
            if r[1] not in U and r[2] not in U: # если обе вершины не соединены, то
                D[r[1]] = [r[1], r[2]]          # формируем в словаре ключ с номерами вершин
                D[r[2]] = D[r[1]]               # и связываем их с одним и тем же списком вершин
            else:                           # иначе
                if not D.get(r[1]):             # если в словаре нет первой вершины, то
                    D[r[2]].append(r[1])        # добавляем в список первую вершину
                    D[r[1]] = D[r[2]]           # и добавляем ключ с номером первой вершины
                else:
                    D[r[1]].append(r[2])        # иначе, все то же самое делаем со второй вершиной
                    D[r[2]] = D[r[1]]

            T.append(r)             # добавляем ребро в остов
            U.add(r[1])             # добавляем вершины в множество U
            U.add(r[2])
        else:
            Rs_additional_reversed.append(r)
    Rs_additional_reversed = sorted(Rs_additional_reversed, key=lambda x: x[0], reverse=True)
    for r in Rs_additional_reversed:    # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[2] not in D[r[1]]:     # если вершины принадлежат разным группам, то объединяем
            T.append(r)             # добавляем ребро в остов
            gr1 = D[r[1]]
            D[r[1]] += D[r[2]]      # объединем списки двух групп вершин
            D[r[2]] += gr1

    #filter(T,lambda cort: True if cort[1]!=cort[2] else False)
    return T
    #print(list(filter(T,lambda cort: True if cort[1]!=cort[2] else False)))

kruskal_alg(R)