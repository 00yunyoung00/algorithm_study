def solution(name):
    answer = 0
    # 알파벳을 움직여야하는 횟수로 바꿔주고 상하로 움직이는 횟수 한번에 더해줌
    name = list(map(lambda x:min(ord(x)-ord('A'),ord('Z')-ord(x)+1),name))
    answer+=sum(name)
    
    # 두가지 경우가 있을 수 있음
    # 한번에 쭉 가느냐
    # 중간에 한번 꺾어서 뒤로가느냐
    # 왔다갔다는 더 많이 이동할 수 밖에 없다
    
    # A들로 끝나는 경우
    # m은 한번에 쭉 가는 경우
    m=len(name)-1
    while m>=0 and name[m]==0:
        m-=1
    if m<0: # 이경우 다 A이다
        return answer
    
    nxt=0
    for i in range(len(name)):
        nxt=i+1
        while nxt<len(name) and name[nxt]==0:
            nxt+=1
        #오른쪽으로 먼저 갔다가 꺾을때
        m=min(m,i*2+len(name)-nxt)
        #먼저 끝으로 꺾었다가 오른쪽으로 갈때
        m=min(m,i+2*(len(name)-nxt))

    answer+=m
    
    return answer