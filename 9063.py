# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n=int(input())
a=[];b=[]
if n >=2:                # 사각형이 나올 최소 n 의 갯수
    for i in range(n):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    c=max(a)-min(a)     # x의 값 중 최댓값-최솟값이 가로 길이
    d=max(b)-min(b)     # y의 값 중 최댓값-최솟값이 세로 길이
    print(c*d)
else:
    print('0')          # n이 2보다 작을 경우 0을 출력
