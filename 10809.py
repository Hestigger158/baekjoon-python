# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명
a = input()
b = 'abcdefghijklmnopqrstuvwxyz'       
for i in b:                           
    if i in a:
        print(a.index(i), end=' ')    # a에 있는 알파벳의 순서를 가로로 나열
    else:
        print(-1, end=' ')
