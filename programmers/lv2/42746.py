# 가장 큰 수

import functools

def comp(a,b):
    t1=a+b
    t2=b+a
    return (int(t1)>int(t2))-(int(t1)<int(t2))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(comp),reverse=True)
    # 0000인 경우가 생길 수 있기 때문에 str->int->str로 처리
    return str(int("".join(numbers)))