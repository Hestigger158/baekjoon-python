# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

a, b, c = map(int, input().split())
s = []
s.append(a)      # 리스트 s에 a, b, c 값 추가
s.append(b)
s.append(c)
s.sort()         # 리스트 s  오름차순으로 정렬
print(s[1])

#다른 방식
a, b, c = map(int, input().split())
s = []
s.append(a)      # 리스트 s에 a, b, c 값 추가
s.append(b)
s.append(c)
s.remove(max(s))  # 리스트에서 중간 값이므로 최댓값 최솟값을 리스트에서 삭제
s.remove(min(s))
print(s[0])
