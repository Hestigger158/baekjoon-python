# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명
a = input()
b = 'abcdefghijklmnopqrstuvwxyz'       
for i in b:                           
    if i in a:
        print(a.index(i), end=' ')    # a에 있는 알파벳의 순서를 가로(end=' ')로 공백을 포함해 나열
    else:
        print(-1, end=' ')            # 포함 되어 있지 않는 경우 '-1' 출
