# 멀쩡한 사각형

# 1. 서로소인 가로세로로 작게 쪼갬
# 2. 그 사각형은 1+(w-1)+(h-1) 만큼의 사각형을 지나서 자름
# 3. gcd만큼 곱해줌 -> 총 지나간 사각형
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def solution(w,h):
    g=gcd(w,h)
    ww,hh=w//g, h//g
    return w*h-g*(ww+hh-1)