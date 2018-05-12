#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/11 21:01'

'''
切割钢条问题：给定一段长度为n英寸的钢条和一个价格表pi(i=0,1,2,3,...,n-1)
求切割钢条方案，使得销售收益最大
'''
'''
复杂度:O(n^2)
n个子问题
每个子问题复杂度为自身规模大小
total:n+(n-1)+(n-2)+...+1=O(n^2)
'''

import math

def memoized_cut_rod(p,n):
    '''
    :param p: type:list,钢条价格
    :param n: type:int;钢条长度
    :param r: type:list;最优收益列表

    :return:
            s: type:list;切割方案
            q: type:int;最优切割收益
    '''
    #初始化r和s
    r = [-1]*(n+1)
    s = [0]*(n+1)
    #返回最大收益值和切割方案
    return memoized_cut_rod_aux(p,n,r,s)

def memoized_cut_rod_aux(p,n,r,s):
    '''
    :param p: type:list,钢条价格
    :param n: type:int;钢条长度
    :param r: type:list;最优收益列表

    :return:
            s: type:list;切割方案
            q: type:int;最优切割收益
    '''
    #如果r[n]>0,说明r[n]这个子问题(长度为n的最大收益值)已经计算过了，不需要重复计算
    if r[n] >= 0:
        return r[n],s
    #基本问题,长度为零，最大收益值为0
    if n==0:
        q=0
    else:
        q=-math.inf
        #for循环，寻找切割点在1,2,3...的最大收益值
        for i in range(n):
            t =  p[i]+memoized_cut_rod_aux(p,n-i-1,r,s)[0]
            if q < t :
                q=t
                s[n] = i+1
    r[n] = q
    return q,s


a=memoized_cut_rod([1,5,8,9,10,17,17,20,24,30],4)#钢条长度为1时卖1块，2时为5块...
print(a)



