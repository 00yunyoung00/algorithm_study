# 짝지어 제거하기

# stack 사용
# 계속 시간초과 나왔는데, 이유는 list slicing때문이었다. st=st[:-1] 으로 구현했는데 매우 느림
def solution(s):
    st=[]
    stl=0
    
    for c in s:
        if stl==0 or st[-1]!=c:
            st.append(c)
            stl+=1
        else:
            st.pop()
            stl-=1
        
    if stl==0:
        return 1
    else:
        return 0