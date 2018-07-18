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
#b记录最优解选择
def bt_up_lcs(X,Y):
    import numpy as np
    m=len(X)
    n=len(Y)
    c=np.zeros((m+1,n+1))
    b=np.zeros((m+1,n+1))
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] ==Y[j-1]:
                c[i,j]=c[i-1,j-1]+1
                b[i,j]=0 #代表xi和yj是一个共同元素
            elif c[i-1,j]>=c[i,j-1]:
                c[i,j]=c[i-1,j]
                b[i,j]=1#代表lcs等同于x[:m-1+1]和y的LCS
            else:
                c[i,j]=c[i,j-1]
                b[i,j]=2#代表lcs等同于x和y[:n-1+1]的LCS
    return c,b

#重构最优解
#复杂度O(m+n)，因为每次递归调用i和j至少有一个会减一
def print_lcs(b,X,i,j):
    if i==0 or j==0:
        return
    if b[i,j]==0:
        print_lcs(b,X,i-1,j-1)
        print(X[i-1],end=' ')
    elif b[i,j]==1:
        print_lcs(b,X,i-1,j)
    else:
        print_lcs(b,X,i,j-1)
c,b=bt_up_lcs('ABCBDAB','BDCABA')
print_lcs(b,'ABCBDAB',7,6)