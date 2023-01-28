# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

a, b = map(int, input().split())
c = list(map(int,input().split())) #주어진 수열을 리스트화
for d in range(a):
    if c[d] < b: # 각 c[0~(a-1)]의 값과 b의 값을 비교
        print(c[d], end=" ") #end=" "를 넣음으로써 가로로 출력하게 만듬
