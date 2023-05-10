# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

while 1:                                   # 조건 없이 무한 반복
    n = int(input())
    if n == -1:
        break                              # 주어진 수가 '-1'일 경우 중지
    else:
        s = []                             # 빈 리스트 생성(약수를 집어넣기 위함)
        for i in range(1,n):
            a = n%i
            if a == 0:                     # 주어진 수를 나눴을 때 0이면 리스트에 그 수(i)를 추가
                s.append(i)
            else:
                pass
        if sum(s) == n:                    # 리스트 합과 주어진 수가 같은경우= 완전수인 경우
            print(n, '=', end=' ')         # 처음엔 주어진 수와 '='을 가로로 출력(이어짐)
            for j in range(len(s)-1):      
                print(s[j], end=' ')       # 1부터 (len(s)-2)까지 s[j]를 가로로 출력(이어짐)....(1)
                if j == (len(s)-1):        # j가 마지막 숫자에 도달 했을 때 정지
                    break
                print('+', end=' ')        # (1) + (1) + (1) +...순으로 나열하게 입력
            print(s[len(s)-1])             # 마지막 숫자는 여백을 비우기 때문에 for문이 끝나고 출력
        else:                              # 완전수가 아닌 경우 주어진 문자를 출력
            print(n , 'is NOT perfect.')
