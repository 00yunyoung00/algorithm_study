# 두 정수 사이의 합

def solution(a, b):
    return (abs(a-b)+1)*(a+b)/2

def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))