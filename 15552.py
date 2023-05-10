# BaekJoon-python-code
learn baekjoon python by my self.


#은 수식 설명

import sys
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())               # 입력받은 두 수를 가로로 출력하는 식
    print(a+b)
    
 #a, b를 사용하지 않고 바로 푸는 방식 
 
import sys
t = int(input())
for i in range(t):
    print(sum(map(int, sys.stdin.readline().split())))
