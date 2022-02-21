# 폰켓몬

def solution(nums):
    answer = 0
    num_set = set(nums)
    
    if len(nums)/2<len(num_set):
        return len(nums)/2
    else:
        return len(num_set)
    
    return answer

def solution(nums):
    return min(len(nums)/2, len(set(nums)))