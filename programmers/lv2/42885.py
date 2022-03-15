# 구명보트

# 인원제한 2명!
# deque사용
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    dq=deque(people)
    while len(dq)!=0:
        if len(dq)==1:
            answer+=1
            break
        if dq[0]+dq[-1]<=limit:
            dq.pop()
            dq.popleft()
            answer+=1
        else:
            dq.pop()
            answer+=1
    
    return answer