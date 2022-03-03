# 124나라의 숫자

def solution(n):
    answer = ''

    while n!=0:
        n-=1
        if n%3==0:
            answer+='1'
        elif n%3==1:
            answer+='2'
        else:
            answer+='4'
        n=n//3
    
    answer=answer[::-1]
    
    return answer