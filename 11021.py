# BaekJoon-python-code
learn baekjoon python by my self.


#은 수식 설명

n=int(input())
i=1
while i <= n:                              # i가 주어진 n보다 작거나 같을 때까지 반복
	a, b=map(int,input().split())          # 더할 두 수 입력
	c=a+b
	print('Case #', end='')                # 출력할 부분 작성 및 공백 없이 가로로 출력
	print(i, end='')
	print(': ',end='')
	print(c)                               # 마지막 이후에는 다음 줄에서 시작하므로 end를 안 넣음 
	i=i+1



#다른 방법
import sys
n =int(input())
for i in range(1,n+1):                                # i가 1부터 n까지 나와야 하므로 range(n)이 아닌 range(1,n+1)을 사용(range(n)=0~(n-1)까지 출력됨)
    a, b =map(int, sys.stdin.readline().split())
    print(f'Case #{i}:', a+b)                         #f'string으로 반복되는 구절을 하나의 식으로 나타내는 것(https://blockdmask.tistory.com/429 참조)
