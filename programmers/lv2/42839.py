# 소수 찾기

from itertools import permutations

def isPrime(num):
    if num==0 or num==1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums=set()
    
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers, i):
            nums.add(int("".join(num)))
            
    nums=sorted(list(nums))
    for num in nums:
        if isPrime(num):
            answer+=1
    
    return answer