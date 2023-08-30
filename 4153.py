# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                                            # 시간절약을 위한 sys 실행
while 1:                                              # 무조건 반복
	l=list(map(int,sys.stdin.readline().split()))     # 리스트에 주어진 3개의 수를 입력
	l.sort()                                          # 오름차순 정렬
	a=int(l[0])                                       # 세 개의 수를 새로운 변수로 지정
	b=int(l[1])
	c=int(l[2])
	if a+b+c==0:                                      # 마지막 0 0 0이 주어지면 종료하게 설정
		break
	else:
		if c**2==a**2+b**2:                           # 직각삼각형이 되는 조건(피타고라스 정리)을 만족하면 right를 출력
			print('right')
		else:
			print('wrong')
