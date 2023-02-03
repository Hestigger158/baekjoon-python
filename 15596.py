# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

def solve(a):         # 기존에 주어진 식
    return sum(a)     # a의 합을 구하면 되므로

# 다른 방식
def solve(a):        # 기존에 주어진 식
    b = 0            # 답을 추출하기 위한 문자
    for i in a:      
        b += i       # i 는 a의 모든 수가 될 때까지 b에 i를 더함
    return b
