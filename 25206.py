# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

# 내가 푼 버전
n = 0.0                              #(학점)
m = 0.0                              #(등급점수)*(학점)
for i in range(20):
	a, b, c= map(str,input().split())
	d=float(b)                         # 학점을 문자열에서 소수점으로 표현하기
	if c == 'P':                       # 등급이 P인 경우 넘기기
		pass
	else:                              # 나머지는 각 등급에 맞는 점수를 (등급점수)*(학점)을 더하기, (학점)은 따로 하나 더 더하기
		if c == 'A+':
			n += d
			m += 4.5 * d
		elif c == 'A0':
			n += d
			m += 4.0 * d
		elif c == 'B+':
			n += d
			m += 3.5 * d
		elif c == 'B0':
			n += d
			m += 3.0 * d
		elif c == 'C+':
			n += d
			m += 2.5 * d
		elif c == 'C0':
			n += d
			m += 2.0 * d
		elif c == 'D+':
			n += d
			m += 1.5 * d
		elif c == 'D0':
			n += d
			m += 1.0 * d
		else:
			n +=d
print(m/n)

# 다른 사람들이 푼 소스(1)

g,s,v=['F','X','D0','D+','C0','C+','B0','B+','A0','A+'],0,0      # g=점수에 대한 리스트화
for i in range(20):
    a,b,c=input().split()
    b=float(b)
    if c!='P':                                                   # (!=같지 않을 경우)
        s+=b
        v+=g.index(c)*b                                          # 리스트g에서 c의 순서값을 더함
print(v/(s*2))                                                   # (리스트g 순서값의 1/2)=(등급점수)를 나타냄

# 다른 사람들이 푼 소스(2)

count = 0
sum = 0
sum2 = 0
for _ in range(20):
    _, a, b = input().split()                                    
    a = float(a)
    if b == 'P': continue                                        # 'P'일 경우 지나침
    match b:                                                     # b(문자열)을 각각의 (숫자)에 매칭시킴
        case 'A+': b = 4.5
        case 'A0': b = 4
        case 'B+': b = 3.5
        case 'B0': b = 3
        case 'C+': b = 2.5
        case 'C0': b = 2
        case 'D+': b = 1.5
        case 'D0': b = 1
        case 'F': b = 0
    sum += a*b
    sum2 += a
print(sum/sum2)
