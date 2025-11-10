import heapq

def add_edge(graph, u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        for neighbor, w in graph[node]:
            new_dist = d + w
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist

def min_delivery_time(graph, start):
    dist = dijkstra(graph, start)
    print(f"Minimum time from {start}:")
    for node, time in dist.items():
        print(f"  {node} → {time} mins")
    print("Total minimum delivery time:", sum(dist.values()), "mins")

def main():
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 5), ('D', 10)],
        'C': [('A', 2), ('B', 5), ('D', 3)],
        'D': [('B', 10), ('C', 3)]
    }

    while True:
        print("\n1. Display Graph\n2. Find Minimum Delivery Time\n3. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            print("\nGraph:", graph)
        elif ch == 2:
            min_delivery_time(graph, 'A')
        elif ch == 3:
            print("Exiting... 🍕")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
