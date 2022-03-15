# 단어 변환

# bfs
from collections import deque

def cmp1(st1, st2):
    cnt=0
    for i in range(len(st1)):
        if st1[i]!=st2[i]:
            cnt+=1
        if cnt>1:
            return False
    if cnt==1:
        return True
    else:
        return False

def solution(begin, target, words):
    cnt = 0        
    dq=deque()
    dq.append([begin,[]])
    
    while dq:
        wrd, path=dq.popleft()
        if wrd==target:
            return len(path)
        for word in words:
            if word not in path and cmp1(wrd, word):
                tmp=path[0:]
                tmp.append(word)
                dq.append([word,tmp])
    
    return 0