def gcs(A:list):
    F = [0 for i in range(0,len(A)+1)]
    print(F)
    for i in range(1, len(A)+1):
        max_ = 0
        for j in range(0,i):
            if A[i-1] > A[j-1] and F[j] > max_:
                max_=F[j]
        F[i] = max_+1
    return F
        
A = [1,2,3,4,10,3,11]
print(gcs(A))