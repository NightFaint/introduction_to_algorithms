#type of input A:list
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        #insert A[j] into the sorted sequence A[0,1,...j-1]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

#test
lst = insertion_sort([1,4,2,5,3])
print(lst)
