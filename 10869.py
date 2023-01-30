 # baekjoon no.10869 website: https://www.acmicpc.net/problem/10869
 
#은 수식 설명

a, b = map(int, input().split())
for op in ['+', '-', '*', r'//', '%']:          #각 사칙연산의 기호를 리스트화
  print(eval(f'{a}{op}{b}'))                    #f'string을 활용해 주어진 a, b값과 위 리스트(사칙연산기호)가 반복되게 설정 후 eval로 계산하게 함
