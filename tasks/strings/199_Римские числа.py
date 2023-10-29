s = input().split('/')

all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def gcd (a:int,b:int) -> int:
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)

def to_roman(num):
    # на старте в римском числе ничего нет
    roman = ''
    # пока наше число больше нуля
    while num > 0:
        # перебираем все пары из словаря
        for i, r in all_roman:
            # пока наше число больше или равно числу из словаря
            while num >= i:
                # добавляем соответствующую букву в римское число
                roman += r
                # вычитаем словарное число из нашего числа
                num -= i
    # как все циклы закончились — возвращаем римское число
    return roman

def recognise(rom):
    # на старте десятичное число равно нулю
    rom_copy = rom
    dec = 0
    # перебираем все пары из словаря
    for i, r in all_roman:
        # пока римское число начинается буквы из словаря
        while rom.startswith(r):
            # увеличиваем десятичное число на соответствующее значение из словаря
            dec += i
            # убираем найденную букву из римского числа
            rom = rom[len(r):]
    # как все циклы закончились — возвращаем десятичное число
    if rom_copy == to_roman(dec):
        return dec
    return 0


def answer(full_str):
    if len(s) !=2:
        return "ERROR"
    first_number = recognise(full_str[0])
    second_number = recognise(full_str[1])
    if first_number* second_number!=0:
        common_del = gcd(first_number,second_number)
        first_number = first_number/common_del
        second_number = second_number / common_del
        if  second_number!=1:
            return to_roman(first_number)+"/"+to_roman(second_number)
        else:
            return  to_roman(first_number)

    return "ERROR"

print(answer(s))

