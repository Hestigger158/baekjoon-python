# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                             # 시간절약을 위한 sys 생성
z=[0 for _ in range(10)]               # 0~9까지 갯수를 세기 위한 리스트 생성(append하는것 보다 이 방법을 사용하는게 시간절약이 됨)
a=int(sys.stdin.readline().strip())    # 주어진 3개의 수를 받음
b=int(sys.stdin.readline().strip())
c=int(sys.stdin.readline().strip())
l=list(str(a*b*c))                     # 그 세 수의 곱을 리스트에 넣음(리스트에 넣으면 각각의 숫자로 분열 됨)
l.sort()                               # 오름차순 정렬
for i in range(len(l)):                # 리스트l의 갯수만큼 반복
	x=int(l[i])                          # 그 숫자를 z의 리스트에 자기 수의 자리에 1을 더함
	z[x]+=1
for j in range(10):                    # z의 각 자리를 출력하는 것을 반복
	print(z[j])
