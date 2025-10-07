def solution(n):
    arr = [[None for _ in range(n)] for _ in range(n)]
    row, col = 0, 0
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    m = 0
    for i in range(1, n**2 + 1):
        arr[row][col] = i
        nr, nc = row + move[m][0], col + move[m][1]
        if not (0 <= nr < n and 0 <= nc < n and arr[nr][nc] is None):
            m = (m + 1) % 4
            nr, nc = row + move[m][0], col + move[m][1]
        row = nr
        col = nc

    return arr

        
print(*solution(5), sep="\n")