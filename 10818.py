# baekjoon-python
learn baekjoon python by my self.

#은 수식설명

z = int(input())
l = list(map(int, input().split()))              #입력된 두번째 줄(z로 첫줄을 처리함) 수를 리스트화
a = min(l)                                       #리스트에 있는 숫자(int)중 작은 수
b = max(l)                                       #리스트에 있는 숫자(int)중 큰 수
print(a, b)
