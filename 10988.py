# baekjoon-python
baek-joon python learn and study my self

#은 수식 설명

# 내가 푼 방식
s = str(input())
a = 0
b = -1
if len(s) == 1:                  # 주어진 단어가 알파벳이 하나일때
    print(1)
else:
    for i in range(len(s)//2):   # 주어진 알파벳의 갯수의 절반만큼 반복
        if s[a] == s[b]:
            a+=1
            b-=1
            if a == len(s)//2:   # a가 단어의 절반에 왔을때(즉, 팰린드롬일때)(홀수인 경우 [len(s)/2]여도 성립하기에 가능함ex. 5/2=2.5이지만 2번째까지만 같아도 팰린드롬임)
                print(1)
            else:                
                pass
        else:
            print(0)
            break                # 단 하나의 0만 출력해야 하기에 break
            
            
           
#다른사람 풀이방법
s = list(str(input()))           # 주어진 단어를 리스트화
if list(reversed(s) == s:        # 거꾸로한 리스트와 리스트가 같은 경우
    print(1)
else:
    print(0)
