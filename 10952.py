# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

import sys
for i in sys.stdin:
    c = sum(map(int, i.split()))
    if c > 0:
        print(c)
    else:
        break
