# 정수 내림차순으로 배치하기

def solution(n):
    return int("".join(sorted(str(int(n)), reverse=True)))