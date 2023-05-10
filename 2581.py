# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

M=int(input())
N=int(input())
a=[]                                    # 빈 리스트 생성
for i in range(M,N+1):                  # 주어진 작은 수(M)부터 큰 수(N)까지 숫자 i 생성
    for j in range(2,i+1):              # 2부터 i까지 인수 생성
        if j==i:                        # j가 i랑 같다면 빈 리스트에 생성
            a.append(i)
        if i%j==0:                      # i를 j로 나눴을 때 나머지가 0이면 중지(소수가 아닌경우를 찾는 법)
            break                       # 첫 번째 if문은 j가 i가 되기 전에는 pass이기에 두번째 if문으로 2부터 i까지 판별
if len(a) < 1:                          # 리스트 a의 갯수가 1보다 작으면 '-1' 출력
    print('-1')
else:                                   # 문제의 조건을 만족한 경우 리스트 a의 합과 최솟값 출력(min(a)도 되고 a[0]도 됨. 그 이유는 작은 값부터 리스트에 집어 넣기 때문에)
    print(sum(a))
    print(min(a))
