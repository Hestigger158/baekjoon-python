# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())
t = n
p = 0                              # 카운트 횟수

while 1:
    a = n // 10                    # n의 앞자리 수
    b = n % 10                     # n의 뒷자리 수
    c = (b * 10) + (a + b) % 10 
    n = c                          # 새로 n의 값을 생성
    p += 1                         # 카운트 횟수 증가
    if c == t: 
     break
print(p)
