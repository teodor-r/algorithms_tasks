
n = int(input())

last_unique = None
counter = 0
ans = []
for i in range(n):
    bit = int(input())
    if bit!= last_unique:
        ans.append(bit)
        last_unique = bit
print(*ans, sep = "\n")
