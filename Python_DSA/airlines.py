
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}
print("Available Routes:")
for city in graph:
    print(city, "->", graph[city])

cities = list(graph)

mid = (low + high) // 2

if cities[mid] == city:
        print("City Found")
        print("Connected Cities:", graph[city])
        break

    elif city < cities[mid]:
        high = mid - 1

    else:
        low = mid + 1

if low > high:
    print("City not found")
