# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a, b, c=map(int, input().split())
d=10000+a*1000                        # 주어진 문제에서의 상금
e=1000+a*100                          # e,f는 a=c 일 때, b=c일 때 나눠서 생성(a=b이면 e=f)
f=1000+b*100
g=max(a, b, c)                        
h=g*100                               # 세개가 다른 수가 나올 때의 상금
if a == b:
 if a == c:
  print(d)
 else:
  print(e)
else:
 if b == c:
  print(f)
 else:
  if a == c:
   print(e)
  else:
   print(h)
