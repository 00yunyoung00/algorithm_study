# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    
    size=len(absolutes)
    for i in range(size):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    
    return answer
    # return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
