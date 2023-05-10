# BaekJoon-python-code
learn baekjoon python by my self.

#은 수식 설명

king, queen, rook, bishop, knight, pawn=map(int,input().split())  # 각 숫자를 체스말에 대입
print(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn)        # 올바른 숫자에서 대입한 숫자를 뺌
