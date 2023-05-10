# BaekJoon-python-code
learn baekjoon python by my self.

#은 수식 설명입니다

n = int(input())
t = int(input())
result = 0
for i in range(t):
    a, b = map(int, input().split())
    result += a*b                          # a*b의 값을 계속 더함 
    
if result == n:                            # 더한 값이 총합과 같다면 yes 출력
    print("Yes")
else:
    print("No")
