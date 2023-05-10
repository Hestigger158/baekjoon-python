# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

a = []                                 # 빈 리스트 생성
b = []
c = []
while 1:                               # while 뒤에 0이 아닌 수를 입력하면 별 다른 조건을 넣지 않는 한 지속됨
    a.append(int(input()))             # 주어진 수를 리스트a에 삽입
    if len(a) == 10:
        break                          # 주어진 수가 10개 이므로 리스트a의 갯수가 10개가 되면 멈추게 함
d = a + b
i = 0
for i in range(10):
    e = d[i] % 42                      # 리스트d에서 순서대로 추출한 것을 42로 나눈 나머지 값을 e로 설정
    c.append(e)                        # e를 리스트c에 삽입
f = list(set(c + b))                   # 리스트에 있는 수 중에 반복되는 수를 제거(set 활용)
print(len(f))
