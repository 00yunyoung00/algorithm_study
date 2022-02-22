# 나누어 떨어지는 숫자 배열

# 파이썬은 or 앞이 거짓일 경우 or 뒤를 리턴
def solution(arr, divisor):

    return sorted([x for x in arr if x % divisor == 0]) or [-1]

