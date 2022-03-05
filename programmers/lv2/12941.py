# 최솟값 만들기

def solution(A,B):

    return sum(list(map(lambda x,y:x*y, sorted(A), sorted(B, reverse=True))))
    

