#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/28 21:28'

from max_heapify import max_heapify
from build_max_heap import build_max_heap

#heap_sort O(nlgn)
def heap_sort(A):
    A_sort=[]
    build_max_heap(A)
    n=len(A)
    for i in range(1,n)[::-1]:
        A[0],A[i]=A[i],A[0]
        current_max=A.pop()
        A_sort.append(current_max)
        max_heapify(A,0)
    return A_sort
A=[16,4,10,14,7,9,3,2,8,1]
A=heap_sort(A)
A