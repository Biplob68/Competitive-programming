def valid(x, y):
    if 0 <= x < col and 0 <= y < row and adjacencyMatrix[x][y] != '#' and visit[x][y] == 0:
        return True
    else:
        return False


def dfs(i, j):
    visit[i][j] = 1
    global count
    count += 1
    for k in range(4):
        x = dx[k] + i
        y = dy[k] + j
        if valid(x, y):
            dfs(x, y)


if __name__ == '__main__':
    T = int(input())
    dx = [+1, -1, +0, -0]
    dy = [+0, -0, +1, -1]

    for case in range(T):
        row, col = map(int, input().split())
        adjacencyMatrix = [input() for _ in range(col)]
        print(adjacencyMatrix)
        visit = [[0 for i in range(row)] for j in range(col)]
        count = 0

        # for i in range(col):
        #     for j in range(row):
        #         adjacencyMatrix[i][j] = input()

        for i in range(col):
            for j in range(row):
                if adjacencyMatrix[i][j] == '@':
                    dfs(i, j)
                    break

        print(f"Case {case + 1}: {count}")
