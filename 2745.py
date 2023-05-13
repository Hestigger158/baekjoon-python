# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n, m= input().split(' ')
n=''.join(reversed(n))    # 주어진 문자(숫자)를 거꾸로 변환
m=int(m)
List="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a=0
for i in range(len(n)-1,-1,-1): #-1을 맨 뒤에 입력하여 뒤에서부터 거꾸로 반복되게 설정(0~5였으면 5~0으로 반복)
	b= List.index(n[i])*(m**i)    #리스트의 값과 주어진 수의 제곱을 곱한값값
	a+=b
print(a)
