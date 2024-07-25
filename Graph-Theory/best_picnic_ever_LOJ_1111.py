from queue import Queue


def bfs(start_city):
    visit = [0 for i in range(cities + 1)]
    global ans
    queue = Queue()
    queue.put(start_city)
    visit[start_city] = 1
    count[start_city] += 1

    if count[start_city] == peoples:
        ans += 1

    while not queue.empty():
        city = queue.get()
        city_list = adjacencyList[city]
        for neighbor_city in city_list:
            if visit[neighbor_city] == 0:
                visit[neighbor_city] = 1
                count[neighbor_city] += 1
                queue.put(neighbor_city)
                if count[neighbor_city] == peoples:
                    ans += 1


if __name__ == '__main__':
    T = int(input())

    for test_case in range(T):
        peoples, cities, roads = map(int, input().split())

        count = [0 for i in range(cities + 1)]
        ans = 0

        adjacencyList = {}
        for city in range(1, cities + 1):
            adjacencyList[city] = []

        people_list = []
        for _ in range(peoples):
            city = int(input())
            people_list.append(city)

        for _ in range(roads):
            x, y = map(int, input().split())
            adjacencyList[x].append(y)
            # adjacencyList[y].append(x)
        for i in range(len(people_list)):
            bfs(people_list[i])
        print(f"Case {test_case + 1}: {ans}")
