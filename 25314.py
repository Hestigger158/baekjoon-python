# baekjoon-python
learn baekjoon python by my self.(백준 독학 저장소)

#은 수식 설명

a = int(input())
b = a // 4             # 주어진 값을 4로 나눈 값
i = 1
c = ''                 # 빈 문자
while i <= b:          # i가 b보다 작을 때
    c += 'long '       # 빈 문자열에 'long '을 추가
    i += 1             
    if i == b+1:       # i가 b+1일 때(i == b가 되고 while 문장을 실행하기 때문에 최종 i값은 b+1이 됨)
        c += 'int'
    else:
        pass
print(c)


# 쉬운 버전
print(int(input())//4*'long ', 'int')
