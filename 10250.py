# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n = int(input())                                # 반복할 변수를 입력
for i in range(n):
    H, W, N = map(int, input().split())         # 주어진 변수 3개를 임의의 문자로 치환
    a = N // H                                  # (승객) // (층수) = (고객이 머물 호수)
    b = N % H                                   # (승객) % (층수) = (고객이 머물 층수), (단, b = 0이 아닌 값일 때 성립)
    if b == 0:                                  # b가 0일 때의 경우
        print(H*100+a)                          # 0이면 꼭대기 층에서 머무는 것이 최단이므로 그 값으로 설정
    else:
        print(b*100+(a+1))                      # 0이 아닌 값은 N / H > N // H 이므로 a의 값에서 1을 더해야 함
