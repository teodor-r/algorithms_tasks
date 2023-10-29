#бинарный поиск,  условия применения - отсортированный массив
# скорость поиска О(log2 N)
def left_bound(A, key):
	left=-1
	right= len(A)
	while right-left>1:
		middle = (left + right)//2
		if A[middle] < key:
			left = middle
		else:
			right = middle
	return left

def right_bound(A, key):
	left=-1
	right= len(A)
	while right-left>1:
		middle = (left + right)//2
		if A[middle] <= key:
			left = middle
		else:
			right = middle
	return right

def binary_search(A, key):
	if (right_bound(A,key) - left_bound(A,key))>1:
		return "Yes"
	return "No"