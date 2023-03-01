# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a, b, c = map(int, input().split())
d = c - a                                   # 마지막 날은 무조건 낮에 도착하므로 낮의 값을 최종 값에서 빼줌
e = d // (a - b)                            # 그 외의 날은 하루(a-b)의 값으로 위의 d값을 나눈 몫(정수, 소수점x)을 구함(이 값이 (정상에 도달하는 날)-1의 값)
if d % (a - b) == 0:                        # 위의 식의 나머지가 없을 경우는 딱 떨어지는 값으로 e+1을 출력
    print(e+1)
else:                                       # 나머지가 있는 경우는 하루를 더 가야 하므로 e+2의 값을 출력
    print(e+2)
