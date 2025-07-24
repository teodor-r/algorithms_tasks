def get_element(A:dict, a_index):
	i =0
	for k,v in A.items():
 		if i == a_index:
 			return {k:v}
 			break
 		else:
 			i+=1


def merge(A:dict, B:dict):
	C={}
	a_index=0
	b_index=0
	while a_index<len(A) and b_index<len(B):
		if(list(A.values())[a_index]<=list(B.values())[b_index]):
			C.update(get_element(A,a_index))
			a_index+=1
 		else:
 			C.update(get_element(B,b_index)) 
 			b_index+=1
	while a_index<len(A):
 		C.update(get_element(A,a_index)); a_index+=1
	while b_index<len(B):
 		C.update(get_element(B,b_index)); b_index+=1;
	return C

def merge_sort(A:dict):
	if len(A)<=1:
		return
	middle = len(A)//2
	L ={}
	R ={}
	for i in range(0,middle):
		L.update(get_element(A,i))
	for i in range(middle,len(A)):
  		R.update(get_element(A,i))
	merge_sort(L)
	merge_sort(R)
	C = merge(L,R)
	A.clear()
	for k,v  in C.items():
		A.update({k:v})
