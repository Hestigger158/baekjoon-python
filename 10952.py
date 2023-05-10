# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

import sys
for i in sys.stdin:
    c = sum(map(int, i.split()))
    if c > 0:                     # 두개의 합이 0보다 클 때
        print(c)
    else:                         # 마지막으로 0 0이 들어오기에 다른 경우 실행
        break
