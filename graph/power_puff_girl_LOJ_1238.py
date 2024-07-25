from queue import Queue


def valid(x, y):
    if (0 <= x < row and 0 <= y < col and adjacencyMatrix[x][y] != '#'
            and adjacencyMatrix[x][y] != 'm'):
        return True
    else:
        return False


def bfs(start_x, start_y, goal_x, goal_y):
    visit = [[0 for i in range(col)] for j in range(row)]
    distance = [[0 for i in range(col + 1)] for j in range(row + 1)]
    queue = Queue()
    queue.put((start_x, start_y))
    visit[start_x][start_y] = 1
    distance[start_x][start_y] = 0

    while not queue.empty():
        xx, yy = queue.get()
        if xx == goal_x and yy == goal_y:
            return distance[xx][yy]

        for k in range(4):
            x = dx[k] + xx
            y = dy[k] + yy
            if valid(x, y) and visit[x][y] == 0:
                queue.put((x, y))
                visit[x][y] = 1
                distance[x][y] = 1 + distance[xx][yy]

    return distance[goal_x][goal_y]


if __name__ == '__main__':
    T = int(input())
    dx = [+1, -1, 0, 0]
    dy = [0, 0, +1, -1]

    for case in range(T):
        row, col = map(int, input().split())
        adjacencyMatrix = [input() for _ in range(row)]
        final_x = 0
        final_y = 0
        for i in range(row):
            for j in range(col):
                if adjacencyMatrix[i][j] == 'h':
                    final_x = i
                    final_y = j
                    break

        ans_list = []
        for i in range(row):
            for j in range(col):
                if adjacencyMatrix[i][j] == 'a':
                    ans_list.append(bfs(i, j, final_x, final_y))
                if adjacencyMatrix[i][j] == 'b':
                    ans_list.append(bfs(i, j, final_x, final_y))
                if adjacencyMatrix[i][j] == 'c':
                    ans_list.append(bfs(i, j, final_x, final_y))

        ans = 0
        for i in range(len(ans_list)):
            ans = max(ans, ans_list[i])
        print(f"Case {case + 1}: {ans}")
