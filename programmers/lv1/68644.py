# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    #set을 사용한 이유 - 중복이 허용되지 않기 때문
    answer = set(answer)
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    
    answer=list(answer)
    answer.sort()
    
    
    return answer