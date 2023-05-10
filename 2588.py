# BaekJoon-python-code
learn baekjoon python by my self.

#는 수식 설명

a, b=int(input()), int(input())
print(a*(b%10))                        # (b%10[(b를 10으로 나눴을 때 나머지 값)=(일의자리)]) (3)의 값
print(a*((b//10)%10))                  # b//10(b를 10으로 나눴을 때 몫(소수점 버림))%10(앞의 값을 10으로 나눴을 때의 나머지 값) (4)의 값
print(a*(b//100%10))                   # b//100(b를 100으로 나눴을 때 몫(소수점 버림))%10(앞의 값을 10으로 나눴을 때의 나머지 값) (5)의 값
print(a*b)                             # (6)의 값
