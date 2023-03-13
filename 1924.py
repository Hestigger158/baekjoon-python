# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a, b = map(int, input().split())
c = a-1                                                       # c{(월)-1}로 지나온 개월을 표시
n = b                                                         # (총 날짜 수)를 다른 문자로 설정
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']       # 요일 리스트 설정
while c > 0:
    if c == 2:                                                # 각 월 마다 추가해야할 날짜를 조건 설정
        n += 28
        c -= 1
    elif c == 4 or c == 6 or c == 9 or c == 11:
        n += 30
        c -= 1
    else:
        n += 31
        c -= 1
date = n % 7                                                  # 총합날짜가 무슨 요일인지 출력(1이 월요일이므로 0은 일요일)
print(day[date])                                              # 그 나머지로 요일 리스트에서 요일 출력
