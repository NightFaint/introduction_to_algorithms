#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/11 22:31'

'''
矩阵链乘法问题：
给定n个矩阵的链(A1,A2,...,An)，矩阵Ai的规模为p(i-1)*pi(1<=i<=n)，求完全括号化方案，使得计算乘积A1A2A3...An所需标量乘法次数最少
'''
'''
计算复杂度：O(n^3)
共有O(n^2)个子问题，m[i,j]:i=1 to n-1;j=2 to n
每个子问题：j-i个选择，最大(n-1)——>O(n)
total：O(n^3)

space complexit：储存m[i,j],s[i,j]。O(n^2)
'''


import numpy as np
import math

def matrix_chain_order(p):
    '''

    :param p: 矩阵链规模list,矩阵Ai的规模为p(i-1)*pi(1<=i<=n)
    :return:m,代价矩阵；m[i,j]表示计算矩阵Ai..j所需标量乘法次数的最小值
            s，最优括号化方案矩阵。s[i,j]保存AiA(i+1)...Aj最优括号括号化方案的分割点位置k
    '''
    n=len(p)-1
    m=np.zeros((n+1,n+1))#多构建了一行一列，为了使下标从1开始
    s=np.zeros((n+1,n+1))#同上
    for l in range(2,n+1):#l表示矩阵链长度
        for i in range(1,n-l+2):#i表示矩阵链的开始位置
            j=i+l-1#j表示矩阵链结束位置
            m[i,j] = math.inf
            for k in range(i,j):#k表示矩阵链分割点位置
                t = m[i,k]+m[k+1,j]+p[i-1]*p[k]*p[j]#每个循环步中，计算m[i,j]时仅依赖于已经计算出的表项m[i,k]和m[k+1,j]
                if m[i,j] > t:
                    m[i,j] = t
                    s[i,j] = k
    m = m[1:,1:]
    s = s[1:,1:]
    return m,s

#构造最优解
def print_optimal_parens(s,i,j):
    if i==j:
        print('A'+str(i+1),end='')#让print输出时不换行
    else:
        print('(',end='')
        print_optimal_parens(s,i,int(s[i,j]-1))#注意，s[i,j]是np.float64对象，不是整数，索引时会出错，必须转换类型
        print_optimal_parens(s,int(s[i,j]),j)
        print(')',end='')


m,s=matrix_chain_order([30,35,15,5,10,20,25])
print(m,'\n',s)
#print(type(b[1,2]))
print_optimal_parens(s,0,5)
