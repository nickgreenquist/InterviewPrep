import heapq

def dijkstras(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    seen = {start: 0}
    path = {}

    while heap:
        current_distance, min_v = heapq.heappop(heap)
        for v in range(len(graph[min_v])):
            if graph[min_v][v] != 0:
                distance = current_distance + graph[min_v][v]
                if v not in seen or distance < seen[v]:
                    seen[v] = distance
                    heapq.heappush(heap, (distance, v))
                    path[v] = min_v
    return seen, path

def shortest_path(graph, start, end):
    seen, path = dijkstras(graph, start)

    if end not in path:
        return None, 0

    final_path = [end]
    v = path[end]
    while v != start:
        final_path.append(v)
        v = path[v]
    final_path.append(start)
    return final_path[::-1], seen[end]


graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

assert shortest_path(graph, 0, 4) == ([0, 7, 6, 5, 4], 21)
assert shortest_path(graph, 4, 0) == ([4, 5, 6, 7, 0], 21)
assert shortest_path(graph, 0, 8) == ([0, 1, 2, 8], 14)
assert shortest_path(graph, 8, 4) == ([8, 2, 5, 4], 16)

print("All assertions pass")
