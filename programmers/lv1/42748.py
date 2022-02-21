# k번째수

def solution(array, commands):
    answer = []
    
    for start, end, idx in commands:
        arr = array[start-1:end]
        arr.sort()
        answer.append(arr[idx-1])
    
    return answer

# 람다식 이용한 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
