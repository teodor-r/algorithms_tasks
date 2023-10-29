
"""
pi_mas -  массив, содержащий значение максимального собственного суффикса,
совпадающего с префиксом для подстроки s[0:i]. То есть   pi_mas[i] - для среза s[0:i] (i -
не включено)
"""

def pi_func(A:str):
    pi_mas = [0] *  (len(A)+1)
    for i in range(1, len(A)): # пробегаем по всем элементам строки
        #s[2] следует рассмотреть срез s[0:2], s[0] + s[1]
        pi_previous_value  = pi_mas[i]
        if  A[i] == A[pi_previous_value]:
            pi_mas[i+1] = pi_previous_value+1
        else:
            while A[i] != A[pi_previous_value] and pi_previous_value > 0:
                pi_previous_value = pi_mas[pi_previous_value]
                if A[i] == A[pi_previous_value]:
                    pi_mas[i+1] = pi_previous_value+1
                else:
                    pi_mas[i + 1] = 0
    print(pi_mas)
    return  pi_mas

def Knut_Morris_Prat(A:str, substring:str):
    result = substring + "#" + A
    pi_mas = pi_func(result)
    end_index =  pi_mas.index(len(substring)) - len(substring) - 1
    return end_index  #первое вхождение

print(Knut_Morris_Prat("abefcdef", "ef"))
#pi_func("######")



