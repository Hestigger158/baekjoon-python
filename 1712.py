# baekjoon-python
learn baekjoon python by my self.(백준 독학 저장소)

#은 수식 설명

# (판매량) = d 라고 하면 a(고정비용) + b(가변비용) * d <= c(가격) * d이므로 d에 관하여 정리하면 d = a /(c - b) 가 나온다
a, b, c = map(int, input().split())              # 주어진 3개의 숫자를 각 문자로 치환
if c <= b:                                       # 위의 식에서 (c - b)가 '0'이 되거나 음수가 되면 손익분기점이 나오지 않기 때문에
    print(-1)
else:
    d = a // (c - b)                             # 판매량의 값을 정수로 치환(ex. 17.56 -> 17)
    print(d + 1)                                 # 소수점이 들어간 판매량보다 크지만 가장 작은 수 이므로 위 식에서 1을 더한 값을 출력
