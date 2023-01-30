# baekjoon-python
learn baekjoon python by my self.

#은 수식설명

z = int(input()) #주어진 숫자 처리용
l = list(map(int, input().split())) # 2번째 줄의 모든 수를 리스트화
a = min(l) #리스트에 있는 숫자(int)중 작은 수 추출
b = max(l) #리스트에 있는 숫자(int)중 큰 수 추출
print(a, b) #(작은수) (큰수)로 표출
