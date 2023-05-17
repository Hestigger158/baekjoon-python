# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a=int(input());b=int(input());c=int(input())
d=set()                                         # 중복된 값은 무시하는 set를 생성
if a+b+c == 180:                                # 주어진 각도의 합이 180인 경우
	d.update([a, b, c])                           # set에 주어진 각도를 집어 넣음 (한개의 값은 add로 여러개의 값은 update로)
	if len(d) ==1:                                # 3개의 각이 똑같을 때, set는 1개만 값을 가짐
		print('Equilateral')
	elif len(d) ==2:                              # 2개의 각이 똑같을 때, set는 2개의 값을 가짐
		print('Isosceles')
	else:                                         # 3개의 각이 다 다른 때, set는 3개의 값을 가짐
		print('Scalene')
else:                                           # 3각의 합이 180이 아닐 때의 경우
	print('Error')
