# N으로 만들기

def solution(N, number):
    answer = 0
    res=[[] for i in range(9)]
    res[1].append(int(N))
    if number==N:
        return 1
    for i in range(2,9):
        res[i].append(res[i-1][0]*10+N)
    
    for i in range(2,9):
        for j in range(1,i):
            for n1 in res[j]:
                for n2 in res[i-j]:
                    res[i].append(n1+n2)
                    res[i].append(n1-n2)
                    res[i].append(n1*n2)
                    if n2!=0:
                        res[i].append(n1//n2)
        if res[i].count(number)!=0:
            return i
    return -1