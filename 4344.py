# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())
for i in range(n):
    b = list(map(int, input().split()))        # 2번째 줄부터 주어진 수를 리스트화
    c = sum(b[1:])/b[0]                        # c(평균)=(리스트b의 1항부터 끝까지 = (점수의 합))/(리스트b의 0항 =(점수의 갯수))
    d = 0                                      # 평균이상의 점수 갯수를 알기 위한 임의의 수 생성
    for e in b[1:]:                            
        if e > c:                              # e의 값이 평균 c의 값보다 높은 경우
            d += 1                             # d의 값을 더함
    a = d / b[0] * 100                         # a = %화 시키기 
    print(f'{a:.3f}%')                         # f'string 활용해서 소수점 3자리 수까지 '%'를 추가해서 출력
