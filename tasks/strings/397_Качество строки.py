s = input()

def ans():
    big_sym = max(s)
    low_sym = min(s)
    if big_sym==low_sym:
        print(low_sym)
        return
    last_sym = None
    min_otrezok = (0,199999)
    for i in range(0,len(s)):
        if (s[i] == big_sym or s[i] == low_sym):
            if last_sym!= None and s[i] != last_sym[0]:
                if i - last_sym[1] < min_otrezok[1] - min_otrezok[0] :
                    min_otrezok = (last_sym[1], i)
            last_sym = (s[i], i)
    print(s[min_otrezok[0]:min_otrezok[1]+1])

ans()