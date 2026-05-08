def dijkstra(graph, start):
    n = len(graph)

    dist = [float("inf")] * n
    prev = [-1] * n
    unvisited = list(range(n))

    dist[start] = 0

    while len(unvisited) > 0:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        for neighbor, weight in graph[current]:
            new_dist = dist[current] + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current

    return dist, prev

# directed graph
graph = [
    [(1, 4), (2, 2)],
    [(2, 1), (3, 5)],
    [(3, 8), (4, 10)],
    [(4, 2)],
    []
]

def distance(graph, start, end):
    dist, _ = dijkstra(graph, start)
    return dist[end] # dist from start to end

dist, prev = dijkstra(graph, 0)

print(dist)
print(prev)