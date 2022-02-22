# 최대공약수와 최소공배수

def solution(n, m):
    a,b=n,m
    
    while a%b!=0:
        a,b=b,a%b

    return [b,n//b*m]