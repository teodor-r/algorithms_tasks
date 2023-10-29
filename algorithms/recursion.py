def pow(a:float, n:int):
	if n==1:
		return a
	elif n%2==1:
		return pow(a,n-1)*a
	else:
		return pow(a**2, n//2)

print(pow(2,10))

#генерация всех чисел  длины M в N-ричной системе счисления
#почему None?Если бы там был пустой список, то питон 
def generate_numbers(N:int , M: int, prefix = []):
	if M==0:
		print(prefix)
		return
	for digit in range(N):
		prefix.append(digit)
		generate_numbers(N,M-1,prefix)
		prefix.pop()

generate_numbers(2,3)

def find(number, A):
	flag = False
	for x in A:
		if x == number:
			flag = True
			break
	return flag

def generate_permuntaions(N:int , M=-1, prefix = None):
	prefix = prefix or []
	M = N if M==-1 else M
	if M==0:
		print(*prefix)
		return
	for number in range(1, N+1):
	 	if find(number,prefix):
	 		continue
	 	prefix.append(number)
	 	generate_permuntaions(N,M-1,prefix)
	 	prefix.pop()

generate_permuntaions(5)