# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                                     
while 1:                                       # 무한 반복(1 또는 True 사용하면 됨 true 아니고 True)
	a=str(sys.stdin.readline().strip())          # 단어가 2개이상일 경우 가로로 출력하도록 입력 조정
	if len(a)==0:                                # 주어진 단어의 갯수가 0일 때, 즉 주어진 값이 더 이상 존재하지 않을 때 멈춤
		break
	print(a)
