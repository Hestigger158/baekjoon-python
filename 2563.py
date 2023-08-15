# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n= int(input())                                         # 몇 번 반복할 지 입력 받기
c=[[0 for _ in range(101)] for _ in range(101)]         # 100*100의 0의 리스트 생성
for cu in range(n):                                     # n번 반복
    a, b=map(int,input().split())
    for y in range(10):                                 # 행의 리스트를 받아서 10의 길이의 행만 반복
        li=c[a+y]                                       # c의 행을 새로운 변수에 지정
        for i in range(10):
            li[b+i-1]=1                                 # 새로운 변수의 행에 열 번호에 10만큼 1로 변경
        c[a+y]=li                                       # 다시 원래 배열에 대입
e=0
for p in range(100):                                    # 각 행의 합을 e에 추가해주는 걸 100번 반복
    d=sum(c[p])
    e += d
print(e)
