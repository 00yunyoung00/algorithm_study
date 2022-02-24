# 기능개발

def solution(N, stages):
    fail = {}
    tot=len(stages)
    for i in range(1,N+1):
        if tot!=0:
            fail[i]=stages.count(i)/tot
            tot-=stages.count(i)
        else:
            fail[i]=0
    
    return sorted(fail, key=lambda x:fail[x], reverse=True)