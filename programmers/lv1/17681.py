# 비밀지도

# 비트연산자 사용하는 방법도 좋을듯
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        line=""
        for j in range(n):
            if arr1[i]%2==0 and arr2[i]%2==0:
                line+=' '
            else:
                line+='#'
            arr1[i]//=2
            arr2[i]//=2
        answer.append(line[::-1])
    
    return answer