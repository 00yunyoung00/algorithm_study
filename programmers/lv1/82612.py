# 부족한 금액 계산하기

def solution(price, money, count):
    
    return max(price*sum(range(count+1))-money,0)


