# 나머지가 1이 되는 수 찾기

def solution(n):
    i=2
    while n%i!=1:
        i+=1
    return i