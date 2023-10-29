s = input()
alpha = {"s":0,"h":0,"e":0,"r":0,"i":0,"f":0}
set_alpha = {"s","h","e","r","i","f"}
for letter in s:
    if letter in set_alpha:
        alpha[letter]+=1

alpha["f"] = alpha["f"]//2

min_letter = min(alpha.keys(), key=lambda k: alpha[k])

print(alpha[min_letter])