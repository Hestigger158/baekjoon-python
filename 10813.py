# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n, m=map(int,input().split())
l=[]                            
l2=l
for i in range(1,n+1):          # 빈 리스트에 1부터 n까지 입력
	l.append(i)
for j in range(m):              # m번 만큼 반복
	a, b=map(int,input().split()) 
	c=l[a-1]                      # 기존 리스트에서 숫자를 받는 법
	d=l[b-1]
	l2[a-1]=d                     # 답 리스트에 변경
	l2[b-1]=c
for k in range(n):              # 답 리스트를 출력
	print(l2[k],end=' ')
