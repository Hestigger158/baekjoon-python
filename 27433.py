# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

def fac(n):               # def로 함수를 정의
    a=n                   # 주어진 숫자와 같은 변수를 생성
    b=1                   # 출력할 값을 생성
    while a>1:            # a가 1보다 큰 경우 계속 반복
        b=b*a             # a의 값을 출력할 값 b에 곱함
        a-=1              # a에 1을 빼고 반복
    return(b)             # 함수의 결과로 b의 값을 출력
c=fac(int(input()))       # 주어진 숫자를 fac에 대입
print(c)                  # 그 값을 출력



# 주어진 문제에서는 for문으로 하지말고 재귀함수를 사용하라고 했음
# 하지만 for문으로도 하는 방법을 작성해 봄

n=int(input())
a=1
for i in range(1,n+1):    # 주어진 숫자만큼 반복
    a=a*i                 # 1부터 n까지 a에 곱합(n>1일 때)
print(a)
