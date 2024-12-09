from queue import Queue


def bfs(grid, r, c):
    q = Queue()
    q.put((r, c))

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    while not q.empty():
        x, y = q.get()

        for index in range(4):
            xx = x + dx[index]
            yy = y + dy[index]
            if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] == "1":
                q.put((xx, yy))
                grid[xx][yy] = "0"


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "1", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    row = len(grid)
    col = len(grid[0])
    island_num = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                island_num += 1
                bfs(grid, i, j)

    print(island_num)
