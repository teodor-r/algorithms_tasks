def generate_permutations(N:int, M:int, prefix=None):
    if  M==0:
        print(*prefix)
        return
    prefix = prefix or []
    for dig in range(N):
        prefix.append(dig)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(11,4)
