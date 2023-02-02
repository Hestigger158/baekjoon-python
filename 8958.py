# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

import sys
input=sys.stdin.readline     #input 값을 추가로 설정(?)
a = int(input())             
for i in range(a):           
    b = 0                    # 0인 값을 설정
    c = 0                    # 0인 값을 설정
    d = list(input())        # O, X를 리스트화
    for t in d:              
        if t == 'O':         # 변수 t의 값이 'O'이면
            c += 1           # c의 값을 더함(계속 진행 되면 c=1-> c=2, 3, 4~a까지 늘어남)
            b += c           # c의 값을 b에 추가함(계속 진행 되면 d=1 -> d=1+2, 1+2+3....늘어난 c의 값의 합을 구하는 것)
        else:                # 변수 t의 값이 'X'일 때
            c = 0            # c의 값을 0으로 초기화
    print(b)

# 이지버전(이해한 식)

n = int(input())                
for i in range(n):
    l = list(input())           # 주어진 O,X를 리스트화
    a = 0                       
    for i in range(len(l)):    
        while 0 <= i:           # 리스트 l의 갯수만큼 반복
            if l[i] == 'O':     # l[i]가 O일 때
                a += 1          # a의 값을 더함
                i -= 1          # i의 값을 뺌(i의 값을 내림으로써, 'while 0 <= i'를 반복을 멈추게 함)
            else:               # l[i]가 X일 때
                break
    print(a)
