#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/5/7 22:04'

#复杂度O(|P|+|T|)
def P_F(P):
    j=0
    i=1
    m = len(P)
    F = ['_'] * m
    F[0] = 0
    while i < m:
        if P[j] == P[i]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j - 1]
        else:
            F[i] = 0
            i += 1
    return F

def KMP_al(P,T):
    F=P_F(P)
    m=len(P)
    n=len(T)
    k=0
    j=0
    Counter=0
    position={}
    while j < n:
        if T[j] == P[k]:
            j += 1
            k += 1
            print('j,k',j,k)
            if k == m:
                print('进入==',j,k)
                position[Counter] = j - k
                Counter += 1
                k = F[k - 1]
        elif k>0:
            print('进入elif,',k)
            k = F[k-1]
        else:
            print('进入else')
            j+=1
    return Counter,position

a,b=KMP_al('sda','sadasda')
print(a,b)
