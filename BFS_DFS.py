from collections import deque
from queue import Queue

from collections import defaultdict
class Graph:
    def __init__(self, numberOfNodes):
        self.nodes = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')[:numberOfNodes]
        self.adj_list = defaultdict(list)

    def getAdjMatrix(self):
        return self.adj_list

    def addEdge(self,u, v):
        self.adj_list[u].append(v)

    def setNodeAsVisited(self, node):
        self.visited[node] = True

    def getNeighbors(self, node):
        node_idx = self.nodes.index(node)
        neighbors = []

        for neighbor_idx in self.adj_list[node_idx]:
            neighbors.append(self.nodes[neighbor_idx])

        return neighbors

    def getNodes(self):
        return self.nodes

graph = Graph(6)

# 0 - A, 1- B, 2-C, 3-D, 4-E, 5-F
# Define Graph
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 5)
graph.addEdge(3, 1)
graph.addEdge(4, 5)
graph.addEdge(5, 2)


def BFS(startNode = 'A'):
    nodes =  graph.getNodes()
    queue = Queue()
    parent = {node: None for node in nodes}
    visited = set()

    queue.put(startNode)

    print("BFS PATH.:", end="")

    while not queue.empty():
        currentNode = queue.get()
        visited.add(currentNode)
        print(currentNode, end='=>')

        for neighbor in graph.getNeighbors(currentNode):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)

    print()



def DFS(startNode = 'A'):
    nodes = graph.getNodes()
    stack = deque()
    parent = {node: None for node in nodes}
    visited = set()

    stack.append(startNode)

    print("DFS PATH.:", end="")

    while not len(stack) == 0:
        currentNode = stack.pop()

        print(currentNode, end='=>')

        visited.add(currentNode)
        
        for neighbor in graph.getNeighbors(currentNode):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    print()


def hasCycles(graph, source, visited, parent):
    visited.add(source)
    for neighbor in graph.getNeighbors(source):
        if not neighbor in visited:
            parent[neighbor] = source
            hasCycles(graph, source=neighbor, visited=visited, parent=parent)
        elif parent[source] != neighbor:
            return True
    return False



BFS()
DFS()
if hasCycles(graph, 'A', set(), { 'A': None }):
    print("This Graph has cycles")
else:
    print("This Graph has no cycles")




