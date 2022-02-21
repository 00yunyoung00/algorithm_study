# 3진법 뒤집기

def solution(n):
    answer = 0
    
    while n/3!=0:
        answer*=3
        answer+=(n%3)
        n//=3
    
    return answer


# int(a,b) = b진법을로 나타낸 string a 를 10진수로
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer