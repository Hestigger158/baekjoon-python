# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a = []                                            # 가장 큰 값을 넣기 위한 리스트 생성
k = 1                                             # 가장 큰 값이 있는 행 번호 생성
s = list(map(int,input().split()))                # 첫 숫자열을 리스트에 생성
b = max(s)                                        # 가장 큰 값을 a에 넣고 index값(열 번호-1)을 j에 대입
a.append(b)
j = s.index(b)
for i in range(2,10):                             # 2번째부터 9번째 행 반복
    t=list(map(int,input().split()))
    c=max(t)
    if a[0] <= c:                                 # 만일 기존에 있던 값보다 새로운 리스트의 최댓값이 클 경우
        a[0] = c                                  # a값 바꾸기
        k = i                                     # k값도 바꾸고 j값도 바꾸기
        j = t.index(c)
        t.clear()                                 # 리스트 초기화
    else:
        t.clear()
print(a[0])                                       # 가장 큰 값 출력
print(k, j+1)                                     # 행, 열 출력
