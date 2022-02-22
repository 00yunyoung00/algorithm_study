# 핸드폰 번호 가리기

def solution(phone_number):
    lst=list(phone_number)
    lst=["*"*(len(lst)-4)]+lst[-4:]
    return "".join(lst)