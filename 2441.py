# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

n = int(input())

s = n
while s > 0:
    print(str('*'*s).rjust(n))     # n개의 칸에서 *을 s개만큼 출력하되, 우측정렬로 출력
    s -= 1
