'''
Задача:найти расстояние Левенштейна между двумя строками
Метод решения: динамическое программирование 
'''


# Пи- функция - ищет наибольный суффикс, являющийся префиксом
# вычисление Пи-функции
s = input()
sub_s = input()
P = [0]*(len(s)+1)
for i in range(2,len(s)+1): 
	if s[i-1] == s[P[i-1]]:
		P[i] = P[i-1]+1
	else:
		m = P[i-1]
		while P[m]>0:
			if s[i-1] == s[P[m]]:
				P[i] = P[m]+1
				break
			else:
				m = P[m]
print(P[len(s)])
print(P)
k=0
l=0
while k<len(s):
	print('k:{0},l:{1}'.format(k,l))
	if s[k]==sub_s[l]:
		k+=1
		l+=1
		if l==len(sub_s):
			print('образ найден, индекс вхождения :',k-l)
			l=0
			continue
	elif l==0:
		k+=1
		if k==len(s):
			print('образ не найден')
			break
	else:
		l=P[l+1]

Ещё
