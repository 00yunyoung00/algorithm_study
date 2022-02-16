# 소수만들기

import math
from itertools import combinations

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True


def solution(nums):
    answer = 0
    
    for a,b,c in list(combinations(nums, 3)):
        if isPrime(a+b+c):
            answer+=1

    return answer