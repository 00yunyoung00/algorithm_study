# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    reward = [6,6,5,4,3,2,1]
    win, zeros = 0,0
    
    for num in lottos:
        if num in win_nums:
            win+=1
        elif num==0:
            zeros+=1
            
    answer.append(reward[win+zeros])
    answer.append(reward[win])
    
    return answer