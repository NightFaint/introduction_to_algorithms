#coding:utf-8
__author__ = 'NightFaint'
__date__ = '2018/7/17 20:07'


def memo_dp():
    memo={}
    def fib(n):
        if n in memo.keys():
            return memo[n]
        else:
            if n<=2:
                return 1
            return fib(n-1)+fib(n-2)
    return fib

def bottom_up_dp(n):
    fib={}
    for i in range(1,n+1):
        if i <=2:
            fib[i]=1
        else:
            fib[i]=fib[i-1]+fib[i-2]
    return fib[n]


a=memo_dp()
result=a(8)
print(result)

b=bottom_up_dp(8)
print(b)