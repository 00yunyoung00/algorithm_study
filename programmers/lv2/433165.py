# 타겟 넘버

answer=0

def dfs(idx, numbers, target, sums):
    global answer
    if idx==len(numbers):
        if sums==target:
            answer+=1
        return
    else:
        dfs(idx+1, numbers, target, sums+numbers[idx])
        dfs(idx+1, numbers, target, sums-numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0,numbers,target,0)
    return answer