#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/12 11:17'

'''
矩阵链乘法问题：
给定n个矩阵的链(A1,A2,...,An)，矩阵Ai的规模为p(i-1)*pi(1<=i<=n)，求完全括号化方案，使得计算乘积A1A2A3...An所需标量乘法次数最少
'''

import numpy as np

def memoized_matrix_chain(p):
    '''

    :param p: 矩阵链规模list,矩阵Ai的规模为p(i-1)*pi(1<=i<=n)
    :return: m[1,n],表示计算矩阵A1..n所需标量乘法次数的最小值
             s:最优括号化方案矩阵。s[i,j]保存AiA(i+1)...Aj最优括号括号化方案的分割点位置k
    '''
    n = len(p)-1
    m = np.zeros((n+1,n+1))
    m[1:,1:]=np.inf
    s = np.zeros((n+1,n+1))
    return lookup_chain(m,s,p,1,n)

def lookup_chain(m,s,p,i,j):
    '''

    :param m: 代价矩阵；m[i,j]表示计算矩阵Ai..j所需标量乘法次数的最小值
    :param s: 最优括号化方案矩阵。s[i,j]保存AiA(i+1)...Aj最优括号括号化方案的分割点位置k
    :param p: 矩阵链规模list,矩阵Ai的规模为p(i-1)*pi(1<=i<=n)
    :param i: 表示矩阵链的开始位置
    :param j: 表示矩阵链结束位置
    :return: m[1,n],表示计算矩阵A1..n所需标量乘法次数的最小值
             s:最优括号化方案矩阵。s[i,j]保存AiA(i+1)...Aj最优括号括号化方案的分割点位置k
    '''

    #m[i,j]<无穷，说明子问题lookup_chain(m,s,p,i,j)已经计算过了，直接返回
    if m[i,j] < np.inf:
        return m[i,j],s
    #i=j，矩阵本身，不需要乘法标量计算，代价为零
    if i == j:
        m[i,j]=0
    else:
        # k表示矩阵链分割点位置
        for k in range(i,j):
            t=lookup_chain(m,s,p,i,k)[0]+lookup_chain(m,s,p,k+1,j)[0]+p[i-1]*p[k]*p[j]
            if m[i,j] > t:
                m[i,j]=t
                s[i,j]=k
    return m[i,j],s

m,s=memoized_matrix_chain([30,35,15,5,10,20,25])
print(m,'\n',s[1:,1:])