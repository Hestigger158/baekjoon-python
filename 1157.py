# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = input().upper()                     # 주어진 알파벳을 대문자로 입력
a = list(set(n))                        # 알파벳을 세트화(겹치는 알파벳 지우는 용)
b = list()                              # 빈 리스트 생성
for i in a:                             
    c = n.count(i)                      # 리스트 n의 알파벳을 세트화한 a에서 각 알파벳의 갯수(c)로 생성
    b.append(c)                         # 리스트 b에 c를 더함(리스트 b = 알바벳의 갯수의 리스트)
if b.count(max(b)) >= 2:                # 리스트 b에서 가장 큰 수의 갯수가 2 이상일 경우
    print('?')
else:
    print(a[(b.index(max(b)))])         # 가장 많은 갯수의 알파벳을 추출
