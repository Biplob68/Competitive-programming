# keep vertices in a set
vertices = {0, 1, 2, 3, 4, 5}

# declare 2d matrix
adjacencyMatrix = [[0 for i in range(6)] for j in range(6)]


def graph_with_matrix(edges):
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        adjacencyMatrix[v1][v2] = 1
        adjacencyMatrix[v2][v1] = 1


# create a dictionary with vertices of graph as keys and empty lists as values
adjacencyList = {}
for vertex in vertices:
    adjacencyList[vertex] = []


def graph_with_dict(edges):
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        adjacencyList[v1].append(v2)
        adjacencyList[v2].append(v1)


if __name__ == '__main__':
    # keep edges in a set
    edges = {(0, 1), (1, 2), (0, 3), (1, 3), (3, 4), (2, 5), (4, 5), (2, 4)}

    graph_with_matrix(edges)
    print("The adjacency matrix representing the graph is:")
    print(adjacencyMatrix)

    graph_with_dict(edges)
    print("The adjacency list representing the graph is:")
    print(adjacencyList)
