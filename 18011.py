# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n, m = map(int, input().split())            # 두 개의 수를 받음
l = []                                      # 빈 리스트를 두 개 생성(하나는 처음 수를 받기 위함, 두 번째는 거꾸로 변환 하기 위한 리스트)
s = []
for i in range(1,n+1):                      # n번 반복하는 동안 빈 리스트 l에 i를 입력
    l.append(i)
for i in range(m):                          # m번 반복
    a, b=map(int,input().split())           # 또 다른 주어진 두 개의 수를 받음
    for j in range((b-a)+1):                # (b-a)+1번 만큼 s에 l[a-1]을 넣고, l[a-1]을 l에서 뺌(그렇게 되면 다음 l[a-1]은 원래 l[a]가 됨)
        s.append(int(l[(a-1)]))
        l.pop((a-1))
    s.reverse()                             # 다 완성한 s를 거꾸로 뒤집음
    for j in range(len(s)):                 # s의 갯수만큼 l에 (a-1)부터 차근차근 삽입함
        l.insert((a-1+j),s[j])
    s.clear()                               # 다 완성 했으면 다음 위의 과정을 반복하기 위해 s를 초기화 시킴
for k in range(len(l)):                     # l의 크기만큼 l의 숫자를 ' '(공백)있이 가로로 출력하게 함
    print(l[k],end=' ')
