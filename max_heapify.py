#-*- coding='utf-8' -*-

#返回左孩子结点
def left(i):
    return 2*i

#返回右孩子结点
def right(i):
    return 2*i+1

#维护最大堆的性质
#type of A:list
#type of i:integer,i>0
def max_heapify(A,i):
    l = left(i)
    r = right(i)
    if l <= len(A) - 1 and A[i] < A[l]:
        largest = l
    else:largest = i
    if r <= len(A) - 1 and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,largest)
    return A 

lst = [1,7,6,5,4,3,2]
lst.insert(0,9)
A=max_heapify(lst,1)
print(A)


