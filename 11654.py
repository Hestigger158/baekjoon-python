# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

a = input()
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"     # 대문자를 나열
if '0' <= a <= '9':                  # a가 숫자일 경우
    print(int(a) + 48)               # 아스키 코드에 맞는 수를 출력
elif "A" <= a <= "Z":                # a가 대문자일 경우
    c = b.index(a)                   # b에서 몇번째 수인지 출력
    print(int(c) + 65)
else:                                # 나머지, 소문자일 경우
    d = b.lower().index(a)           # 나열된 값을 소문자로 변환 후 몇번째 수인지 출력
    print(int(d) + 97)
