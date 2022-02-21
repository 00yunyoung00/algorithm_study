# 체육복

def solution(n, lost, reserve):
    lost_n = list(set(lost)-set(reserve))
    reserve_n = list(set(reserve)-set(lost))
    
    answer = n-len(lost_n)
    num_reserve = len(reserve_n)
    
    for s in lost_n:
        if s-1 in reserve_n:
            reserve_n.remove(s-1)
        elif s+1 in reserve_n:
            reserve_n.remove(s+1)
            
    answer+=num_reserve-len(reserve_n)

    return answer