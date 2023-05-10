# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())
for i in range(n):
    a, b = input().split()          # a(숫자), b(문자열)로 지정
    c = ""                          # 답을 나열할 빈 항목
    for l in b:                     # b에서 각 항목 추출
        for i in range(int(a)):    
            c += l                  # 빈 항목에 추출한 항목을 a만큼 더함
    print(c)
