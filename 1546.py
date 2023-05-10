# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())                        
a = list(map(int, input().split()))          #두번째 주어진 수를 리스트에 삽입
print(sum(a) / max(a) * 100 / n)
