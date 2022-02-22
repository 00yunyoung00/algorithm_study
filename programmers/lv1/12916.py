# 문자열 내 p와 y의 개수

def solution(s):
    cnt=0
    
    for c in s:
        if c=='P' or c=='p':
            cnt+=1
        elif c=='Y' or c=='y':
            cnt-=1

    return cnt==0

# count함수 사용
def solution(s):
    return s.lower().count('p')==s.lower().count('y')