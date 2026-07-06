# 18.Check whether there is a direct edge between two given vertices.

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

v1 = "A"
v2 = "B"

if v2 in graph[v1]:
    print("Edge exists")
else:
    print("Edge does not exist")