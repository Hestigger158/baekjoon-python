# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

# 주어진 수의 곱이 양수일때 1,3사분면, 음수면 2,4사분면으로 풀 때
a=int(input())
b=int(input())

if a*b > 0:       
    if a>0:
        print('1')
    else:
        print('3')
else:
    if a>0:
        print('4')
    else:
        print('2')
    
# 둘 중 하나의 값을 기준으로 풀 때  
a, b=int(input()), int(input())
if a > 0:
   if b > 0:
       print('1')
   else:
       print('4')
else:
   if b > 0:
       print('2')
   else:
       print('3')
