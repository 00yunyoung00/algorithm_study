# 전화번호 목록

# 정렬하면 바로 다음거만 봐도 된다구~
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return answer