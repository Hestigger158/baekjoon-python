# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n = int(input())
if n == 1 or n == 2 or n == 4 or n == 7:       # 5 와 3으로 나누어 떨어지지 않는 수
    print('-1')
else:
    if n%5 == 0:                               # 5로 나누었을 때 나머지가 0인경우
        print(n//5)
    elif n%5 == 1:                             # 5로 나누었을 때 나머지가 1인 경우
        print((n-6)//5+2)                      # 6은 5로 나누었을 때 나머지가 1이므로 주어진 값에 6을 빼고 5로 나눈뒤 3kg의 갯수 2개를 더함
    elif n%5 == 2:                             
        print((n-12)//5+4)                     # 나머지가 2인경우는 12이므로 위와 똑같이 해주면 됨
    elif n%5 == 3:
        print((n-3)//5+1)                      
    else:
        print((n-9)//5+3)
