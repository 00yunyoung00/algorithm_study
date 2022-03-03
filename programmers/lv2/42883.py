# 큰 수 만들기

def solution(number, k):

    number=list(map(lambda x:int(x),number))
    
    # 앞에서부터, 다음 숫자보다 내가 작으면 버린다
    st=[]
    for i in range(len(number)):
        if(k==0):
            st.extend(number[i:])
            break
        while len(st)>0 and st[-1]<number[i] and k>0:
            st.pop()
            k-=1
        st.append(number[i])
    
    # 다 돌았는데 k가 남았으면 끝에서부터 버림
    while k>0:
        st.pop()
        k-=1
        
    return "".join(list(map(lambda x:str(x), st)))