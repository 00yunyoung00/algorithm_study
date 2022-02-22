# 짝수와 홀수

def solution(num):
    #return "Even" if num%2==0 else "Odd"
    return ["Even", "Odd"][num&1] 
    # 비트연산자 활용