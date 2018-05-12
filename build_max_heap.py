from max_heapify import max_heapify
from math import floor

def build_max_heap(A):
    A_heap_size = len(A)
    for i  in range(1,floor(A_heap_size/2)+1)[::-1]:
        max_heapify(A,i)