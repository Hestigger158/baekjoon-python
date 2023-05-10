# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n, k = map(int, input().split())
a = []                                    # 약수를 집어넣기 위한 빈 리스트
for i in range(1,n+1):                    # 1부터 n까지 반복문
    b = n%i                               # n(주어진 수)를 i로 나눴을 때 나머지
    if b == 0:                            # 나머지가 0일 때 리스트 a에 나머지가 0이되는 i 값을 추가
        a.append(i)
    else:                                
        pass
if len(a) < k:                            # (리스트a의 원소갯수) < (주어진 수) 일때는 0을 추출
    print('0')
else:                                     # 리스트에서 k-1번째 원소를 추출(리스트는 0부터 추출)
    print(a[k-1])
