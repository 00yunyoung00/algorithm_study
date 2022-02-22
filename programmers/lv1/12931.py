# 자릿수 더하기

def solution(n):
    answer = 0
    
    n=str(n)
    for c in n:
        answer+=int(c)

    return answer



def solution(n):

    n=list(str(n))

    return sum(int(x) for x in n)