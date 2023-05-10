# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명
while 1:                                   # 정해지지 않은 횟수의 반복일 경우, 'while'을 사용(정해진 경우 'for'을 사용)( 1,True 같은 것은 제한 없이 반복)
    a, b = map(int, input().split())
    if a == b:                             # 문제에서 같은 숫자는 나오지 않는다고 했기에, 마지막에 나오는 0, 0일 경우 정지시키게 함
        break
    else:
        c = a%b                            # a를 b로 나눈 나머지의 값(0일 경우 배수의 관계)
        d = b%a                            # b를 a로 나눈 나머지의 값(0일 경우 약수의 관계)
        if c == 0:
            print('multiple')              # 배수를 출력
        elif d == 0:
            print('factor')                # 약수를 출력
        else:
            print('neither')               # 서로소를 출력
