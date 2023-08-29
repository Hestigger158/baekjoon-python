# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                                         # 시간절약을 위한 것
a=sys.stdin.readline().strip()
b=list(map(int, sys.stdin.readline().split()))     # 주어진 배열을 리스트에 집어 넣음
b.sort()                                           # 최소시간을 알기 위해서는 오름차순 정렬을 해야함
c=int(0)                                           # 총 걸리는 시간을 위한 0 생성
for i in range(len(b)):                            # 리스트 b의 길이만큼 반복함. 각 항마다 첫번째부터 i번째까지 더해줘야함
	for j in range(i+1):
		c+=b[j]
print(c)	                                         # 총 걸린 시간을 출력
