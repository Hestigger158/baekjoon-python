# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a,b=map(int,input().split())          # 주어진 수를 입력을 받음
c=int(input())
d=int(input())
if c*d < a*d+b or c*100 < a*100+b:    # 주어진 공식을 만족하지 않을 경우 a,b는 정수이므로 음수일 경우엔 가장 큰 수인 100일때도 만족하게 설정 함
	print(0)
else:                                 # 올바른 경우 1을 출력
	print(1)
