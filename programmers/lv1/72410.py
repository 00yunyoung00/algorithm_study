# 신규 아이디 추천
# 여러가지 string처리
# 정규식으로 푸는 방법도 있음

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id=new_id.lower()
    
    # 2단계
    for char in new_id:
        if char.isalnum() or char in ['-','_','.']:
            answer+=char
    
    # 3단계
    while ".." in answer:
        answer=answer.replace("..", ".")
    
    # 4단계
    if answer.startswith('.'):
        answer=answer[1:]
    if answer.endswith('.'):
        answer=answer[:-1]
    
    # 5단계
    if len(answer)==0:
        answer="a"
    
    # 6단계
    if len(answer)>15:
        answer=answer[:15]
    if answer[-1]=='.':
        answer=answer[:-1]
    
    # 7단계
    while len(answer)<3:
        answer+=answer[-1]
    
    return answer