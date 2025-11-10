class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_matrix = [[0]*nodes for _ in range(nodes)]  # For DFS
        self.adj_list = [[] for _ in range(nodes)]            # For BFS

    def add_edge(self, u, v):
        # Adjacency Matrix (for DFS)
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

        # Adjacency List (for BFS)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start, visited):
        print(chr(start + 65), end=" ")
        visited[start] = True
        for i in range(self.nodes):
            if self.adj_matrix[start][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    def bfs(self, start):
        visited = [False] * self.nodes
        queue = Queue()
        queue.enqueue(start)
        visited[start] = True

        print("BFS Traversal (Adjacency List): ", end="")
        while not queue.is_empty():
            node = queue.dequeue()
            print(chr(node + 65), end=" ")
            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.enqueue(neighbour)
        print()


# --- main part ---
g = Graph(5)  # 5 nodes: A, B, C, D, E

# sample connections (like city locations)
g.add_edge(0, 1)  # A-B
g.add_edge(0, 2)  # A-C
g.add_edge(1, 3)  # B-D
g.add_edge(2, 4)  # C-E

# DFS using adjacency matrix
print("DFS Traversal (Adjacency Matrix): ", end="")
visited = [False] * 5
g.dfs(0, visited)  # start from A (index 0)
print()

# BFS using adjacency list
g.bfs(0)  # start from A
