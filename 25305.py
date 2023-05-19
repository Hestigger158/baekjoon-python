# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a,b=map(int,input().split())
c=list(map(int,input().split()))   # 주어진 점수를 리스트에 입력
for i in range(b-1):               # b-1번 만큼 반복
    c.remove(max(c))               # 리스트에 가장 큰 값을 제거
print(max(c))                      # 커트라인 값을 출력
