# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                              # 시간 절약을 위한 방법(input대신에 sys.stdin.readline()활용)
a= int(sys.stdin.readline())
y=[]                                    # 수의 입력을 받았을 때 넣을 빈 리스트 생성
for i in range(a):                      
	b=sys.stdin.readline()                # a번만큼 반복할 때, b를 입력 받음
	k=b.split()                           # b를 split()함('1 x'일 경우 [1,x]로 분할 됨)
	if len(k)==2:                         # split한 경우 k의 원소 갯수가 2일 경우 k[1]을 빈 리스트에 추가
		y.append(k[1])
	else:                                 # 하나의 수만 입력받아진 경우
		if k[0]=='2':                       
			if len(y)> 0:                     # 2를 받을 경우 비어있지 않으면 y의 마지막 수를 출력하고 그 수를 뺌
				print(y[(len(y)-1)])
				y.pop((len(y)-1))
			else:                             # 비어있다면 -1을 출력
				print('-1')
		elif k[0]=='3':                     # 3을 받을 경우 y의 원소 갯수를 출력
			print(len(y))
		elif k[0]=='4':                     # 4를 받을 경우 비어있지 않으면 0을 출력, 아닌 경우 -1을 출력
			if len(y)> 0:
				print('0')
			else:
				print('1')
		else:                               # 나머지, 즉 5를 받을 경우도 비어있지 않으면 y의 마지막 수를 출력, 비어있다면 -1을 출력
			if len(y)> 0:
				print(y[(len(y)-1)])
			else:
				print('-1')
