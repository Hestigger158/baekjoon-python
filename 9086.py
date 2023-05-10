# baekjoon-python
learn baekjoon python by my self.(백준 독학 저장소)

#은 수식 설명

n = int(input())
for i in range(n):         # n번 반복
    a = str(input())       # 문자열 입력
    print(a[0]+a[-1])      # 그 문자의 첫번째([0])와 마지막([-1])을 입력하되 빈칸 없이(+) 출력
