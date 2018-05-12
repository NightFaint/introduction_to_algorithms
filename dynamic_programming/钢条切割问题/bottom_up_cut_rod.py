#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/11 22:05'

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

def bottom_up_cut_rod(p,n):
    '''
    :param p: type:list,钢条价格
    :param n: type:int;钢条长度
    :param r: type:list;最优收益列表

    :return:
            s: type:list;切割方案
            r[n]: type:int;最优切割收益
    '''
    #创建r[0,...n]来保存子问题的最大收益值和s[0,...n]来保存子问题的最佳切割方案
    r = [-1] * (n+1)
    s = [0] * (n+1)
    #长度为零的钢条没有收益
    r[0] = 0
    #第一个for循环对i=1,2,3,...n按升序求解每个规模为i的子问题。
    #第二个for循环求解长度为i的钢条在哪切割收益值最大
    for i in range(1,1+n):
        q=-math.inf
        for j in range(i):
            t = p[j] + r [i-j-1]
            if q < t:
                q = t
                s[i]=j+1
        r[i]=q
    return r[n],s
a=bottom_up_cut_rod([1,5,8,9,10,17,17,20,24,30],4)
print(a)