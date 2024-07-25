from collections import defaultdict
from queue import Queue


def isBiColor(adjacencyList, startNode):
    queue = Queue()

    queue.put(startNode)
    color[startNode] = 1

    while not queue.empty():
        node = queue.get()
        neighbors = adjacencyList[node]
        for neighbor in neighbors:
            if color[neighbor] == 0:
                color[neighbor] = - color[node]
                queue.put(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True


if __name__ == '__main__':
    while True:
        nodes = int(input())
        edges = int(input())

        adjacencyList = defaultdict(list)
        color = [0] * (nodes * nodes)

        for i in range(edges):
            node1 = int(input())
            node2 = int(input())
            adjacencyList[node1].append(node2)
            adjacencyList[node2].append(node1)

        if not isBiColor(adjacencyList, 0):
            print("NOT BICOLORABLE.")
        else:
            print("BICOLORABLE.")
