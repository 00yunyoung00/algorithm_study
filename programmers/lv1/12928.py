# 약수의 합

import math

def solution(n):
    answer = 0
    
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            answer+=i
            answer+=(n//i)
            print(i)
            
    if n**0.5==int(n**0.5):
        answer-=math.sqrt(n)
    
    return answer