# 내적
# zip함수 - 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
def solution(a, b):
    return sum(at*bt for at, bt in zip(a, b))