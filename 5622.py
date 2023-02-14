# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

a = input()
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']      # 각 전화번호에 있는 알파벳을 리스트화
c = 0
for n in range(len(a)):                                            
    for i in b:                                                      
        if a[n] in i:                                               # a[n]이 i(b의 각 목록)에 포함될 경우
            c += b.index(i) + 3                                     # 리스트 b에서 i의 항번호에 3을 더함
print(c)
