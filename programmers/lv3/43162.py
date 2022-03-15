# 네트워크

#bfs
def solution(n, computers):
    answer = 0
    net=[-1 for i in range(n)]

    def bfs(idx,cnt):
        net[idx]=cnt
        for i in range(n):
            if net[i]==-1 and computers[idx][i]==1:
                bfs(i,cnt)
    
    while net.count(-1)!=0:
        answer+=1
        bfs(net.index(-1), answer)
        
    
    return answer