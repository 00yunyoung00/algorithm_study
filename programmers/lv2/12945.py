# 피보나치 수

def solution(n):
    p, answer=0,1

    for i in range(2,n+1):
        p,answer=answer,(answer+p)%1234567
    
    return answer