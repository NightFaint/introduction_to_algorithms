# -*-coding:utf-8 -*-

def merge(A,p,q,r):

    n1 = q - p + 1
    n2 = r - q
    lst1 = [0] * (n1+1)
    lst2 = [0] * (n2+2)
    for i in range(n1):
        lst1[i] = A[p+i]

    for j in range(n2):
        lst2[j] = A[q+j+1]
    lst1[n1] = 10**8
    lst2[n2] = 10**8
    i = 0
    j = 0
    for k in range(p,r+1):
        if lst1[i] <= lst2[j]:
            A[k] = lst1[i]
            i=i+1
        else:
            A[k] = lst2[j]
            print('A[',k,']=',A[k])
            j+=1
    print('进入merge:',A,p,r)
    return A

import math

def merge_sort(A,p,r):
    print('进入',A,p,r)
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    else:
        print(A[p])
        return A[p]
    return A

A=[2,3,5,4,8,1,6]
A=merge_sort(A,0,6)
print(A)
