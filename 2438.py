# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())
for a in range(n):
    print('*' *(a+1))   # a=0부터 n-1까지이므로 a+1을 해줌
    
# a를 1부터 n까지 출력하고 싶다면
for a in range(1,n+1):
    print('*'*a)
