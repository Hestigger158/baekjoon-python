# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n = int(input())              
ans = set()                  # 빈 세트 생성(원래 세트는 {}인데 빈 세트 생성하려면 set()로 생성, {}는 dict으로 인식함)(리스트도 가능, 리스트는 중복o, 세트는 중복x)
for i in range(n):
    a = int(input())         
    ans.add(a)               # 입력 받은 값을 n번만큼 빈 세트 ans에 추가
for j in range(n):
    print(min(ans))          # set ans에서 작은 값을 추출
    ans.remove(min(ans))     # set ans에서 작은 값을 삭제
