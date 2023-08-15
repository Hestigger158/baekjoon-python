# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                                # 빠른 계산을 위한 sys 추가
a=int(sys.stdin.readline())               # input()보다 sys.stdin.readline()이 더 빠르게 받음
b=[0 for i in range(a)]                   # 빈 리스트에 append 하는 것 보다 0개의 리스트를 만들고 각 번호의 값을 바꾸는게 시간이 빠름
for i in range(a):
    b[i]=int(sys.stdin.readline())        # a만큼 반복할때 각 번호를 순서대로 집어넣음
    if i == a-1:                          # 마지막에 실행하게 만듬
        b.sort()                          # 오름차순 정렬
        for j in range(len(b)):           # 넣은 리스트 갯수만큼 반복
            print(b[j])                   # 순서대로 출력
    else:                                 # 그게 아니면 pass
        pass
