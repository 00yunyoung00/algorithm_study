# 시저 암호

# ord() : char to ascii
# "".join(list) : lst to string
def solution(s, n):
    lst = list(s)
    
    for i in range(len(lst)):
        if lst[i].isupper():
            lst[i]=chr((ord(lst[i])-ord('A')+n)%26+ord('A'))
        elif lst[i].islower():
            lst[i]=chr((ord(lst[i])-ord('a')+n)%26+ord('a'))

    return "".join(lst)