# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    l=[3,0]
    r=[3,0]
    
    for num in numbers:
        if num in [1,4,7]:
            answer+='L'
            l=[(num-1)//3,0]
        elif num in [3,6,9]:
            answer+='R'
            r=[(num-3)//3,0]
        else:
            if num==0:
                num=11
            if abs(l[0]-(num-2)//3)+abs(-l[1]+1)<abs(r[0]-(num-2)//3)+abs(-r[1]+1):
                answer+='L'
                l=[(num-2)//3,1]
            elif abs(l[0]-(num-2)//3)+abs(-l[1]+1)>abs(r[0]-(num-2)//3)+abs(-r[1]+1):
                answer+='R'
                r=[(num-2)//3,1]
            else:
                if hand=="left":
                    answer+='L'
                    l=[(num-2)//3,1]
                else:
                    answer+='R'
                    r=[(num-2)//3,1]
    
    return answer