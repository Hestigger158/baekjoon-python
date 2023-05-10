# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n=int(input())
i=1
a=2
while i <=n:
  b=2*a-1      #규칙성 구현
  # 초기상태의 한 변의 점 갯수(a_0)가 2인데 a_1번은 2+(2-1)=3개
  # a_2번은 3+(3-1)=5이므로 a_n번째는 a_(n-1)+(a_(n-1)-1)이다 
  i=i+1
  a=a*0+b      # 규칙성을 위해 a를 b의 값으로 변형
c=b**2         # 점의 갯수 가로*세로(제곱 표현**)
print(c)
