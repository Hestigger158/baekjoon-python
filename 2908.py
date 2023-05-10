# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

# 기존 풀이
a, b = map(int, input().split())
c = a % 10 * 100 + a // 10 % 10 *10 + a // 100          # 각 자리수 구하고 거꾸로 가게 설정
d = b % 10 * 100 + b // 10 % 10 *10 + b // 100
if c > d:
    print(c)
else:
    print(d)
   
# 쉬운 풀이 
a, b = map(str, input().split())       # [::-1]은 int는 안 되기 때문에 str로 설정
c = a[::-1]                            # [::-1]이 뒤에서부터 나열(거꾸로 나열)
d = b[::-1]
if c > d:
    print(c)
else:
    print(d)
