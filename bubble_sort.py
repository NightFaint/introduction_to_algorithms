def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
    return A

A=[4,6,3,8,5,2]
A=bubble_sort(A)
print(A)
