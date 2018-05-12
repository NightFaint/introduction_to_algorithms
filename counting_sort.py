def counting_sort(A):
    C=[0]*(max(A)+1)
    B=[0]*len(A)
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1,max(A)+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)):
        B[C[A[j]]-1] = A[j]
        #print(B[C[A[j]]])
        C[A[j]] -= 1
    return B 
A=counting_sort([2,3,1,4,6,3,6])
print(A)
