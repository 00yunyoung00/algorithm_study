# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    st=[]
    l=len(board[0])
    ll=len(board)
    boards = [[0 for i in range(ll)] for j in range(l)]
    
    for i in range(ll):
        for j in range(l):
            boards[j][ll-i-1]=board[i][j]

    for move in moves:
        while len(boards[move-1])!=0 and boards[move-1][-1]==0:
            boards[move-1].pop()
        if len(boards[move-1])==0:
            continue
        elif len(st)!=0 and st[-1]==boards[move-1][-1]:
            st.pop()
            boards[move-1].pop()
            answer+=2
        else:
            st.append(boards[move-1].pop())
    
    return answer