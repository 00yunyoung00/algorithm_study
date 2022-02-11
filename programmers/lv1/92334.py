# 신고 결과 받기
# dictionary, set, string split 사용

def solution(id_list, report, k):
    answer = []
    ans={}
    report_to = {}
    report_from = {}
    
    # 신고 하나씩 확인하면서, 신고받은 유저에 해당하는 딕셔너리에 신고한 유저 추가
    for list in report:
        str1, str2 = list.split()
        if str2 not in report_from:
            report_from[str2]=[]
        if str1 not in report_from[str2]:
            report_from[str2].append(str1)
    
    # 신고받은 유저 딕셔너리 돌면서 
    # 경고를 날릴 유저를 신고한 유저는 메일을 받아야하기 때문에 카운트 하나씩 올려줌
    for report_user in report_from:
        if len(report_from[report_user])>=k:
            for user in report_from[report_user]:
                if user not in ans:
                    ans[user]=0
                ans[user]+=1
                
    # id_list에 있는 유저 순서대로 return해야하기 때문에 딕셔너리에서 하나씩 찾아본다
    for id in id_list:
        if id not in ans:
            answer.append(0)
        else:
            answer.append(ans[id])
                    
    return answer


# 하는 일은 똑같지만 더 짧고 간단한 풀이
def best_solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    # report 돌면서 신고받은 유저 카운트를 올림
    # set() 을 사용해 report에서 중복을 없앰
    for r in set(report):
        reports[r.split()[1]] += 1

    # 다시 report돌면서 k이상의 신고를 받은 유저에 대해
    # 이 유저를 신고한 유저의 카운트를 올림
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
