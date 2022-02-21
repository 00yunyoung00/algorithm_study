# 숫자 문자열과 영단어

def solution(s):
    answer = 0
    
    s=s.replace("one", "1")
    s=s.replace("two", "2")
    s=s.replace("three", "3")
    s=s.replace("four", "4")
    s=s.replace("five", "5")
    s=s.replace("six", "6")
    s=s.replace("seven", "7")
    s=s.replace("eight", "8")
    s=s.replace("nine", "9")
    s=s.replace("zero", "0")

    return int(s)


num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def solution(s):
    answer = 0
    
    for eng, num in num_dic.items():
        s=s.replace(eng, num)

    return int(s)