# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a=[]
b=[]
for i in range(3):
	n,m=map(int,input().split())
	a.append(n)
	b.append(m)
if a[0] == a[1]:                 # a에 같은 수가 있는 경우 그 경우를 제외한 원소를 출력
	print(a[2], end=' ')
elif a[1] == a[2]:
	print(a[0], end=' ')
else:
	print(a[1], end=' ')
if b[0]==b[1]:                  # b에 같은 수가 있는 경우 그 경우를 제외한 원소를 출력
	print(b[2])
elif b[1]==b[2]:
	print(b[0])
else:
	print(b[1])
  
  
  
# 조금 압축한 경우
a=[]
b=[]
for i in range(3):
    n,m=map(int,input().split())
    if n in a:                    # 리스트 a에 n의 원소가 있는 경우
        a.remove(n)
    else:
        a.append(n)
    if m in b:                    # 리스트 b에 m의 원소가 있는 경우
        b.remove(m)
    else:
        b.append(m)
print(a[0],b[0])                  # 남은 원소를 출력


# def 활용
a=[]; b=[]
def find(n,m):                    # n에 m의 존재 유무에 따른 행동을 입력한 find(n,m)을 정의
    if m in m:
        n.remove(m)
    else:
        n.appen(m)
for i in range(3):                # 3개의 점을 find(n,m)에 넣고 결과를 리스트 a,b에 입력
    c,d=map(int,input().split())
    find(a,c);find(b,d)
print(a[0], b[0])                 # 남은 값을 출력
