# baekjoon-python
learn baekjoon python by my self.

#은 수식 설명

n = int(input())
l = list(map(int, input().split()))                    # (주어진 문제의 2번째 줄의 숫자)를 리스트화
a = int(input())                                       # (주어진 문제의 3번째 줄)=(찾고자 하는 값)
print(l.count(a))                                      # count안에 a의 값을 넣음으로서, 리스트에서 a의 값의 갯수 만큼 출력
