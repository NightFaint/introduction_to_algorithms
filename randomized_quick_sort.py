from numpy import random
from quick_sort import partition

def randomized_partition(A,p,r):
    i = random.randint(p,r+1)
    A[i],A[r-1] = A[r-1],A[i]
    return partition(A,p,r)

def randomized_quick_sort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r)
        randomized_quick_sort(A,p,q-1)
        randomized_quick_sort(A,q+1,r)
A = [2, 8, 7, 1, 3, 5, 6, 4]
randomized_quick_sort(A, 0, 7)
