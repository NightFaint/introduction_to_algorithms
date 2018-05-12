#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/12 15:33'

'''
最长公共子序列问题：给定两个序列X=(x1,x2,...,xm)和Y=(y1,y2,...,yn)。求X和Y长度最长的公共子序列。
共有O(m*n)个子问题，c(i,j)表示X[:i+1]和Y[:j+1]的lcs长度。i=0 to m,j=0 to j。共(1+m)*(1+n)个
每个子问题计算时间为O(1)
total complexity:O(m*n)
space complexity:O(m*n)
'''

import numpy as np
def lcs_length(x,y):
    m=len(x)
    n=len(y)
    c=np.zeros((m+1,n+1))
    c[:,0]=0
    c[0,:]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                c[i,j]=c[i-1,j-1]+1

            elif c[i-1,j]>=c[i,j-1]:
                c[i,j]=c[i-1,j]

            else:
                c[i,j]=c[i,j-1]

    return c

a=lcs_length('ABCBDAB','BDCABA')
print(a)