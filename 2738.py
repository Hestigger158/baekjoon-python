# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

m,n = map(int,input().split())                # n*m의 행렬을 구성할 n,m을 받음
s1 = []                                       # 빈 리스트 생성
s2 = []
s=[]
for i in range(m):
    l=list(map(int,input().split()))          # 가로로 있는 숫자를 리스트에 추가
    s1.append(l)                              # 그 리스트를 새로운 리스트에 집어 넣음
for i in range(m):                            # 두 번째 행렬도 똑같은 과정을 반복
    o=list(map(int,input().split()))
    s2.append(o)
for i in range(m):                            # m줄동안 n개의 수가 있는 행렬 두개를 각 자리의 합을 새로운 리스트에 입력
    for j in range(n):
        s.append(s1[i][j]+s2[i][j])
for k in range(len(s)):                       # 행렬로 출력하기 위해서 if문으로 (k+1)이 n개로 나눴을 때 나머지가 0이면 새로운 줄에 숫자를 출력 아닌경우 가로로 출력함
    if (k+1)%n==0:
        print(s[k])
    else:
        print(s[k],end=' ')
