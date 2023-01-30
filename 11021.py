# BaekJoon-python-code
learn baekjoon python by my self.


#은 수식 설명

import sys
n =int(input())
for i in range(1,n+1):                                # i가 1부터 n까지 나와야 하므로 range(n)이 아닌 range(1,n+1)을 사용(range(n)=0~(n-1)까지 출력됨)
    a, b =map(int, sys.stdin.readline().split())
    print(f'Case #{i}:', a+b)                         #f'string으로 반복되는 구절을 하나의 식으로 나타내는 것(https://blockdmask.tistory.com/429 참조)
