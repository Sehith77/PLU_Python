# graph = {
#     "A": ["B", "E"],
#     "B": ["C", "D"],
#     "C": ["B"],
#     "D": ["A", "C"],
#     "E": ["B", "C"]
# }

# print(graph)

# matrix = [
# # A  B  C  D  E
#   [0, 1, 0, 0, 1],  
#   [0, 0, 1, 1, 0],  
#   [0, 1, 0, 0, 0],  
#   [1, 0, 1, 0, 0],  
#   [0, 1, 1, 0, 0]   
# ]

# for row in matrix:
#     print(row)

GLOBAL_DICT = {}

class Node:
    def __init__(self, data):
        self.data = data


class Graph:
    def generate(self, data):
        new_node = Node(data)
        return new_node

    def generate_rel(self, node1, node2):
        if node1.data not in GLOBAL_DICT:
            GLOBAL_DICT[node1.data] = []

        GLOBAL_DICT[node1.data].append(node2.data)


g = Graph()


node1 = g.generate("A")
node2 = g.generate("B")
node3 = g.generate("C")

