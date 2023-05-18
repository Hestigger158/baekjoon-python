# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a,b,c=map(int,input().split())
n=[a,b,c]                         # 주어진 숫자를 리스트화
m=max(n)                          # 가장 큰 변의 길이를 다른 변수로 생성 
if m >= sum(n)-m:                 # 세 변의 길이로 삼각형이 이루어지지 않을 경우
	print(2*(sum(n)-m)-1)         # 다른 두 변의 길이의 합보다 1 작은 값으로 설정하여 둘레를 출력
else:                             # 삼각형이 이루어지는 경우는 그대로 둘레를 출력
	print(sum(n))
