# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

import sys                                             # input()대신 시간을 줄이기 위한 방법 
a,b=map(int,sys.stdin.readline().split())              # 두개의 수를 받기 위함
a1=set(map(int,sys.stdin.readline().split()))          # 각 집합을 set에 받음
a2=set(map(int,sys.stdin.readline().split()))
b1=a1-a2                                               # 차집합을 생성
b2=a2-a1
print(len(b1)+len(b2))                                 # 대칭 차집합의 수를 출력

# set는 중복된 수를 제거하는데 문제에서는 중복된 수에 대한 얘기가 없는데도 맞는 결과가 나왔음. 아마 집합이라 그런것일지도 모르겠습니다.
