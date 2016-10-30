def dijkstra(graph, start, end):
    queue = []
    seen = set()
    h.heappush(queue, (0, start))

    while len(queue) > 0:
        d, n = h.heappop(queue)
        
        if n == end:
            return d

        if n in seen:
            continue
        seen.add(n)

        children = (c for c in graph[n].keys() if c not in seen)
        for c in children:
            h.heappush(queue, (d + graph[n][c], c))

    return False