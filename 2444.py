# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n = int(input())
for i in range(n):
    a = "*"*((i+1)*2-1)         # 맨 위부터 나열 될 *의 갯수
    print(a.rjust(n+i))         # 우측정렬로 좌측에만 빈 공간을 나열
j = n
while j >=2:
    c = "*"*((j-1)*2-1)         # n+1번째 줄부터 나열 될 *의 갯수
    print(c.rjust(n+j-2))       # 우측 정렬로 좌측에만 빈 공간을 나열
    j -= 1
