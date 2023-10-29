def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
          z[i] += 1
        if i + z[i] > right:
          left, right = i, i + z[i]
    return z
# отпимизировать цикл, тогда по времени дудет проходить
def answer():
    initial_word = input()
    answer = input()
    if len(answer)!= len(initial_word):
        print("No")
        return
    result = answer + "#" + initial_word
    z = z_func(result)
    delim_index = len(answer)
    len_r = len(result)
    for i in range(delim_index+1, len_r):
        if z[i] == len_r - i:
            if  result[delim_index+1:i][::-1] == result[delim_index-(i-delim_index)+1:delim_index]:
                print("Yes")
                print(delim_index - z[i], end='')
                return
    print("No")

answer()
