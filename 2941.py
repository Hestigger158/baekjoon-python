# baekjoon-python
learn baekjoon python by my self.(백준 독학 저장소)

#은 수식 설명

a = input()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']     # 크로아티아 알파벳을 리스트화
c = 0
for i in b:                                               
    while i in a:                                         # i(리스트 b의 요소)가 a(주어진 문자열)에 있을 때
        c += a.count(i)                                   # a에 속한 i의 갯수만큼 추가
        a = a.replace(i,'0'*len(i))                       # a에 있는 i를 다른문자('0')로 교체
print(c + len(a)-a.count('0'))                            # c(a에 속한 b의 수) + (a의 문자 수) - (a에 있는 문자'0'의 수)
