# есть много реализаций быстрых сортировок
# сортировка слиянием, гарантиравана временная сложность O(n log n)
# сортировка называется устойчивой, если она не меняет 
# порядок равных элементов
# лишь функция слияния
def merge(A:list, B:list):
	C=[0]* (len(A)+len(B))
	a_index=0
	b_index=0
	c_index=0
	while a_index<len(A) and b_index<len(B):
 		if(A[a_index]<=B[b_index]):
 			C[c_index]=A[a_index]
 			c_index+=1; a_index+=1
 		else:
 			C[c_index]=B[b_index]
 			c_index+=1; b_index+=1
	while a_index<len(A):
 		C[c_index]=A[a_index]; a_index+=1;c_index+=1
	while b_index<len(B):
 		C[c_index]=B[b_index]; b_index+=1;c_index+=1
	return C
#можно сделать и другой интерфейс, где merge будет принимать
#единственный массив и индексы частей кусков, которые будут
#сливаться
# функция сортировки
# важная замечание: всегда у рекуррентой функции есть 
# особенный случай, с него всегда и нужно начинать
# реализацию функции
def merge_sort(A):
	if len(A)<=1:
		return
	middle = len(A)//2
	L = [A[i] for i in range(0,middle)]
	R = [A[i] for i in range(middle,len(A))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L,R)
	for i in range(len(A)):
		print(len(A))
		A[i] = C[i]
B = [1, 20 ,1 , 0 , 13, 100]
merge_sort(B)
print(B)

#сортировка Тони Хоара(quick_sort)
def hoar_sort(A):
	if len(A)<=1:
		return
	barrier= A[0]; L=[];M=[];R=[];
	for x in A:
		if x < barrier:
			L.append(x)
		elif x== barrier:
			M.append(x)
		else:
			R.append(x)
	hoar_sot(L)
	hoar_sot(R)
	A=L+M+R

