from collections import defaultdict
from queue import Queue


def numberOfProvinces(n):
    visit[n] = 1
    q = Queue()
    q.put(n)

    while not q.empty():
        v = q.get()
        for neighbor in adj_list[v]:
            if visit[neighbor] == 0:
                q.put(neighbor)
                visit[neighbor] = 1


if __name__ == '__main__':
    isConnected = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]
    ]

    adj_list = defaultdict(list)

    nodes = len(isConnected)
    visit = [0] * (nodes + 2)
    cnt = 0

    for row in range(nodes):
        for col in range(nodes):
            if isConnected[row][col] == 1:
                adj_list[row + 1].append(col + 1)

    for node in range(1, nodes + 1):
        if visit[node] == 0:
            cnt += 1
            numberOfProvinces(node)

    print(cnt)
