import heapq

# Graph definition
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic function
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))
    closed_set = set()

    while open_list:
        f, g, current_node, path = heapq.heappop(open_list)

        if current_node == goal:
            print(f"Path found: {' -> '.join(path)} with total cost: {g}")
            return path

        if current_node in closed_set:
            continue
        closed_set.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_set:
                total_cost = g + cost
                heapq.heappush(open_list, (
                    total_cost + heuristics[neighbor],
                    total_cost,
                    neighbor,
                    path + [neighbor]
                ))

    print("Goal not reachable.")
    return None

# Run A*
start, goal = 'S', 'G'
a_star(graph, heuristics, start, goal)
