# 다트 게임

# 약간 빡구현..?
# 10을 다른 문자로 치환한 후 보는 방법 사용하면 좋을듯
def solution(dartResult):
    answer = 0
    point=0
    prev=0
    prevc=''
    for c in dartResult:
        if c.isdigit():
            if prevc.isdigit() and c=='0':
                point*=10
            else:
                answer+=point
                prev=point
                point=int(c)
        elif c=='D':
            point**=2
        elif c=='T':
            point**=3
        elif c=='*':
            answer+=prev
            point*=2
        elif c=='#':
            point*=-1
        prevc=c
    answer+=point
    return answer