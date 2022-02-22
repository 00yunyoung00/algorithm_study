# 이상한 문자 만들기 

# enumerate 사용
# s를 공백으로 자른 리스트의 항목들을 x로 받아옴. enumerate(x)한 값들을 idx i와 value a로 하나씩 돌겠다
def solution(s):
    
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

