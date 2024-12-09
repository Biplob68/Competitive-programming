from queue import Queue


def bfs(grid, r, c):
    q = Queue()
    q.put((r, c))

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    grid[r][c] = 0
    area_cnt = 1

    while not q.empty():
        x, y = q.get()

        for index in range(4):
            xx = x + dx[index]
            yy = y + dy[index]
            if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] == 1:
                area_cnt += 1
                q.put((xx, yy))
                grid[xx][yy] = 0

    return area_cnt


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    row = len(grid)
    col = len(grid[0])
    max_island = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                max_island = max(max_island, bfs(grid, i, j))

    print(max_island)
