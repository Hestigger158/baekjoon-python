# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n, m = map(int,input().split())          #
l=list('0'*n)                            # n개의 0을 가진 리스트 생성
for i in range(m):                       # m번 만큼 반복문 생성
    a, b, c = map(int,input().split())
    for j in range(b-a+1):               # b-a+1만큼 숫자가 변경되어야 하므로 반복문 생성
        l[a-1+j]=c                       # a-1+j의 항이 주어진 c의 값으로 변경함
for k in range(n):
    print(l[k], end=' ')                 # 마지막의 리스트 l의 각 항을 순서에 맞게 가로로 나
