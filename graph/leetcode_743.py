from queue import Queue


def networkDelayTime(k):
    visit = set()

    q = Queue()
    adj = {}
    for node in range(1, node_num + 1):
        adj[node] = []

    for u, v, w in node_list:
        adj[u].append((v, w))

    q.put((k, 0))
    delay = 0

    while not q.empty():
        node, time = q.get()

        if node in visit: continue
        visit.add(node)
        delay = max(delay, time)
        neigh = adj[node]

        for v, w in neigh:
            if v not in visit:
                new_time = time + w
                q.put((v, new_time))

    if node_num == len(visit):
        return delay
    else:
        return -1


if __name__ == '__main__':
    node_list = [[1, 2, 1]]
    node_num = 2
    start_node = 1

    ans = networkDelayTime(start_node)
    print(ans)
