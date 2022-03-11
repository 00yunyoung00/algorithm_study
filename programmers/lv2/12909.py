# 올바른 괄호

# 아래 코드는 스택 사용
def solution(s):
    s=list(s)
    st=[]
    
    for c in s:
        if c=='(':
            st.append('(')
        else:
            if len(st)==0:
                return False
            else:
                st.pop()
                
    if len(st)==0:
        return True
    
    return False

# 스택사용x 카운트
def solution(s):
    s=list(s)
    cnt=0    
    for c in s:
        if c=='(':
            cnt+=1
        else:
            if cnt==0:
                return False
            else:
                cnt-=1
                
    if cnt==0:
        return True
    
    return False