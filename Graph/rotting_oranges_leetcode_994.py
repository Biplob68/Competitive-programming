from queue import Queue


def bfs(grid):
    q = Queue()

    row = len(grid)
    col = len(grid[0])
    fresh_org = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                q.put((i, j))
            elif grid[i][j] == 1:
                fresh_org += 1

    min_minutes = 0

    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]

    while not q.empty() and fresh_org > 0:
        k = q.qsize()
        min_minutes += 1

        while k > 0:
            x, y = q.get()

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] == 1:
                    fresh_org -= 1
                    q.put((xx, yy))
                    grid[xx][yy] = 2
            k -= 1

    return min_minutes if fresh_org == 0 else -1


if __name__ == '__main__':
    isConnected = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    minimum_minutes = bfs(isConnected)
    print(minimum_minutes)
