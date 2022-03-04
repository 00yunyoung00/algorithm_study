# N개의 최소공배수

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def solution(arr):
    
    tmp=arr[0]/gcd(arr[0],arr[1])*arr[1]
        
    for i in range(2,len(arr)):
        tmp=tmp//gcd(tmp,arr[i])*arr[i]
    
    return tmp