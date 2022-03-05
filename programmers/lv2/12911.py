# 다음 큰 숫자

# 하나씩 더하며 1개수 같은 수 찾는방법 말고 시간 적게쓰는 다른방법 
def solution(n):
    answer = 0
    lst=[]

    # 이진수로 바꿈(뒤집어져있음)
    while n!=0:
        lst.append(n%2)
        n//=2

    # 끝에서부터 처음 1다음 0나오는곳 찾아감 
    # 얘는 그 앞이 0이거나 없거나
    idx=1
    cnt=lst[0]
    while idx<len(lst):
        if lst[idx-1]==1 and lst[idx]==0:
            break
        if lst[idx]==1:
            cnt+=1
        idx+=1
    
    if idx==len(lst):            
        # 없으면 마지막 1만 하나 밀고 1들을 뒤쪽으로 밀어버림
        lst.append(1)
        for i in range(cnt-1):
            lst[i]=1
        for i in range(cnt-1, len(lst)-1):
            lst[i]=0
    else:
        # 0이면 바로 앞(idx) 1로 채우고 뒤에 1 다 뒤로밀어버림
        lst[idx]=1
        for i in range(cnt-1):
            lst[i]=1
        for i in range(cnt-1,idx):
            lst[i]=0
    
    #다시 10진수로
    for i in lst[::-1]:
        answer*=2
        answer+=i
    
    return answer