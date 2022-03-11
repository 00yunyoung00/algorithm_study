# 게임 맵 최단거리

from collections import deque

def solution(maps):
    # bfs는 재귀보다 반복문으로 구현하자
    answer = 1
    n=len(maps)
    m=len(maps[0])
    
    dxdy=[[1,0],[-1,0],[0,1],[0,-1]]
    deq=deque()
    
    deq.append([0,0,1])
    maps[0][0]=0
    
    while len(deq)!=0:
        x,y,cnt=deq.popleft()
        if x==n-1 and y==m-1:
            return cnt
        else:
            for dx,dy in dxdy:
                if x+dx in range(0,n) and y+dy in range(0,m) and maps[x+dx][y+dy]==1:
                    deq.append([x+dx,y+dy,cnt+1])
                    maps[x+dx][y+dy]=0
    
    return -1