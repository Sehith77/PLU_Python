# 19.Perform a Breadth-First Search (BFS) traversal starting from vertex A.

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

visited = []
queue = ["A"]

while queue:
    node = queue.pop(0)

    if node not in visited:
        print(node)
        visited.append(node)
        queue.extend(graph[node])
        