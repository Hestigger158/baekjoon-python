# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

l=[]                                         # 주어진 글자를 넣기 위한 리스트 생성
for i in range(5):
    s=list(input())
    l.append(s)                              # 5줄 동안 글자를 리스트 추가
t=[]                                         # 그 리스트의 나열된 숫자를 알기위한 리스트 생성
for i in range(5):
    t.append(len(l[i]))                      # 각 줄의 갯수를 리스트에 추가
for n in range(max(t)):                      # 가장 큰 갯수만큼 반복
    for i in range(5):                       # 5줄 동안 반복
        if n+1 <= len(l[i]):                 # 각 줄의 갯수보다 출력할 줄의 숫자가 작거나 같을 경우
            print(l[i][n],end='')            # 그 리스트의 i번째와 n번째의 글자를 출력
        else:                                # 아닌 경우 pass
            pass
