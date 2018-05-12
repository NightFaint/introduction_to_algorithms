#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/12 16:03'

import numpy as np
def optimal_bst(p,q,n):
    e=np.zeros((n+2,n+1))
    w=np.zeros((n+2,n+1))
    root=np.zeros((n+1,n+1))
    for i in range(1,n+2):
        e[i,i-1] = q[i-1]
        w[i,i-1] = q[i-1]
    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            e[i,j]=np.inf
            w[i,j]=w[i,j-1]+p[j-1]+q[j]
            for r in range(i,j+1):
                t = e[i,r-1]+e[r+1,j]+w[i,j]
                if t<e[i,j]:
                    e[i,j]=t
                    root[i,j]=r
    return e[1:,:],root[1:,1:]
a=optimal_bst([0.15,0.1,0.05,0.1,0.2],[0.05,0.1,0.05,0.05,0.05,0.10],5)
print(a)
