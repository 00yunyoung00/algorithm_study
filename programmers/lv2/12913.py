# 땅따먹기

def solution(land):
    # 쌓아주는 방법  
    for i in range(len(land)-1):
        for j in range(4): 
            land[i+1][j]+=max(list(filter(lambda x:x[0]!=j, enumerate(land[i]))), key=lambda x:x[1])[1]
            
    return max(land[len(land)-1])