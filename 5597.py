# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = 1
a = []                                  # 빈 리스트 생성
b = []                                  # 빈 리스트 생성
for x in range(1, 31): 
    a.append(x)                         # 숫자 1~30까지 리스트 a에 추가
c = a + b                               # 리스트 a를 빈 리스트와 합쳐서 하나의 리스트로 생성(print(a)하면 30개 나오기 때문에 하나로 합치는 과정)
for y in range(28):                     # 28명만 제출 했음
    c.remove(int(input()))              # 주어진 값을 리스트c에서 제거
d = c + b                               # 위와 마찬가지로 리스트 c를 빈 리스트와 합쳐서 다시 하나의 리스트로 생성
print(min(d))                           # 리스트 d에서 가장 작은 값 추출
print(max(d))                           # 리스트 d에서 가장 큰 값 추출 
