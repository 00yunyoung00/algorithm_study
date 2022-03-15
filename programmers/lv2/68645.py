# 삼각 달팽이

def solution(n):
    answer = [[0 for i in range(1,j+1)] for j in range(1,n+1)]
    cnt=1
    
    for i in range(1,n+1):
        if i%3==1:
            # /
            for j in range((i//3)*2, (i//3)*2+n):
                answer[j][i//3]=cnt
                cnt+=1
            n-=1
        elif i%3==2:
            # --
            for j in range(i//3+1,i//3+1+n):
                answer[len(answer)-i//3-1][j]=cnt
                cnt+=1
            n-=1
        else:
            # \
            for j in range(len(answer)-i//3-1, len(answer)-i//3-1-n, -1):
                answer[j][len(answer[j])-i//3]=cnt
                cnt+=1
            n-=1
    
    return sum(answer, [])