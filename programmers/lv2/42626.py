# 더 맵게

import heapq as hq
# 꼭 heqp 사용해야 효율성 통과하는듯
def solution(scoville, K):
    answer = 0

    hq.heapify(scoville)

    while scoville[0]<K:
        if len(scoville)==1:
            return -1
        else:
            hq.heappush(scoville, hq.heappop(scoville)+2*hq.heappop(scoville))
            answer+=1
            
    return answer