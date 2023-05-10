# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())                             
a = 0
for i in range(1, n+1):                      # 1부터 n까지 나열
    if i < 100:                              # 1부터 99까지는 각 자리수 차가 일정하기 때문에 등차수열에 해당함
        a += 1
    else:
        b = list(map(int, str(i)))           # 100이상부터는 각 자리 수를 리스트화
        if b[0] - b[1] == b[1] - b[2]:       # 각 자리수가 등차수열이 성립하는지에 대한 if문 작성
            a += 1
print(a)
