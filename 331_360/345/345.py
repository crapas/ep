with open("m1", "r") as rp:
    lines = rp.readlines()
board = []

for line in lines:
    line = line.strip().replace("  ", " ").replace("  ", " ")
    segs = line.split(" ")
    a_line = []
    for seg in segs:
        a_line.append(int(seg))
    print(a_line)
    board.append(a_line)

print(board[0][0])
print(board[0][1])

def max_sum(a1, b1, a2, b2):
    print(a1, b1, a2, b2)
    if a1 + 1 == a2:
        # 1 vertical line
        max_v = 0
        for i in range(b1, b2):
            if board[a1][i] > max_v:
                max_v = board[a1][i]
        print("1 : ", max_v)
        return max_v
    if b1 + 1 == b2:
        max_v = 0
        for i in range(a1, a2):
            if board[i][b1] > max_v:
                max_v = board[i][b1]
        print("2 : ", max_v)
        return max_v
    sum = 0
    for i in range(a1, a2):
        t_sum = board[i][b1] 
    max_sum(a1 + 1, b1, a2, b2)

width = len(board[0])
height = len(board)
max_sum(0, 0, width, height)

