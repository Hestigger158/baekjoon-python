# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys               
a=sys.stdin.readline()     # 빠른 입력 받기를 위함(input()대신 더 빠르게 받음)
l=list(a)                  # 주어진 수를 하나씩 split 하는 방법이 리스트에 대입
l.sort(reverse=True)       # 오름차순으로 정렬
for i in range(len(l)):    # 리스트의 원소 수 만큼 반복
	print(l[i],end='')       # 공백없이 가로로 출력
