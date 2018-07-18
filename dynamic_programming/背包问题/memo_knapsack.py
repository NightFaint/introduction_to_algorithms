#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/7/18 21:50'

def memo_knapsack(v,s,S):
    n=len(v)
    c=np.zeros((n+1,S+1))
    return assist(v,s,c,0,S)

def assist(v,s,c,i,j):
    if c[i,j]>0:
        return c[i,j]
    elif i==len(v):
        return 0
    else:
        q=0
        if s[i]<=j:
            q=v[i]+assist(v,s,c,i+1,j-s[i])
        c[i,j]=max(q,assist(v,s,c,i+1,j))
    return c[i,j]
a=memo_knapsack([1,2,3,4],[1,2,3,5],9)
print(a)