# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

h, m=map(int,input().split())
if m >= 45:                     # 45분 보다 큰 경우 시각은 그대로 출력, 분만 45 빼고 출력
   print(h, m-45)
else:
   if h == 0:                   # 0시 인 경우 23시가 되기 때문에 따로 출력 
      print(23, 15+m)
   else:                        # 다른 경우는 시각에 -1을 해줌
       print(h-1, 15+m)
