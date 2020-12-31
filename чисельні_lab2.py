# def f(x_x):
#     return x_x * x_x * x_x - x_x * x_x + 3


# try:
#     e = float(input("Enter e: "))
# except ValueError:
#     e = 0.0000001

# try:
#     a, b = tuple(map(lambda element: float(element), input("Enter interval for x: ").split(" ")))
# except ValueError:
#     a, b = -2, 0

# iteration = 0
# x = 0
# while (b - a) > 2 * e:
#     x = (b + a) / 2
#     fa = f(a)
#     fx = f(x)
#     if fx * fa > 0:
#         a = x
#     else:
#         b = x
#     iteration += 1

# print("Evaluated x: ", x)

# print("number of iterations: ", iteration)

# print("check : ", f(x))





def bfs(graph: list, start_vertex: int):
    visited = [False for x in graph]
    distances = [None for x in graph]
    distances[start_vertex] = 0
    vertex_to_visit_queue = []
    vertex_to_visit_queue.append(start_vertex)
    while vertex_to_visit_queue:
        current_vertex = vertex_to_visit_queue.pop(0)

        for neighbour in graph[current_vertex]:
            # if neighbour vertex is black - ignore it
            if visited[neighbour]:
                continue

            # calculate distances
            if distances[neighbour] is not None:
                distances[neighbour] = min(distances[current_vertex] + 1, distances[neighbour])
            else:
                distances[neighbour] = distances[current_vertex] + 1
            
            # mark child vertex as grey

            # visited[neighbour] = True
            
            vertex_to_visit_queue.append(neighbour)

        # mark vertex as black
        visited[current_vertex] = True
    return distances

graph = [[1], [2,3],[1,3,4,5], [1,2,6], [2], [2], [3,7,8], [6], [6]]
print(bfs(graph, 0))

