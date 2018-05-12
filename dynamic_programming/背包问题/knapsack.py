#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/12 20:45'

'''
背包问题：一个背包能容纳S公斤物品；现有n件物品，各自的价值为v0,v1,v2,...,v(n-1)，重量为s0,s1,..,s(n-1)
求背包所能带的物品的最大价值
复杂度：O(n*S)
'''

import numpy as np

def knapsack(v,s,S):
    '''

    :param v:价值列表
    :param s: 重量列表
    :param S: 限重S公斤
    :return: 所能带的最大价值
    '''
    n=len(v)
    c =np.zeros((n+1,S+1))#c[i,j]表示一个子问题，从第i个物品开始（视第0个物品为第一个物品），限重j公斤，所能带的物品的最大值
                          #共(n+1)*(S+1)个子问题
    #基本问题c[n,j],j=0 to S,表示限重j公斤，从第n个物品（为空）开始，所能带的物品最大值为零（没东西可以带）
    for i in range(n)[::-1]:#从第n-1个物品开始
        for j in range(S+1):#限重0，,,,，S公斤
            #是否要带s[i]，v[i]的物品
            t=0
            if j>=s[i]:
                t=v[i]+c[i+1,j-s[i]]
            c[i,j] = max(c[i+1,j],t)
    return c[0,S]

a=knapsack([1,2,3,4],[1,2,3,5],9)
print(a)