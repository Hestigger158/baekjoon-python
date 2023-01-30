# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

i = 0
a = []                                              # 빈 리스트 생성
for c in range(9):
    a.append(int(input()))                          # 각각의 값을 하나씩 리스트에 추가
while i <= 8:                                       # a[i] = a[8]이 될 때까지
  if a[i] == max(a):                                # a[i]가 리스트a 중 가장 큰 값과 같을 때
    print(max(a))                                   # 리스트 a 중 가장 큰 값 출력
    print(i+1)                                      # 가장 큰 값의 번호의 줄을 출력
  i += 1                                            # [i = i+ 1]과 동일한 수식, 더 간단 함. 계속 증가하는 것을 의미
