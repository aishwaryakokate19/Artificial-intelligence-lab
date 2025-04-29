from collections import deque

# Recursive BFS function
def recursive_bfs(graph, queue, visited):
    if not queue:
        return

    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)

    recursive_bfs(graph, queue, visited)

# Main function
def main():
    # Get number of nodes
    n = int(input("Enter number of nodes: "))
    graph = {}

    # Input graph connections
    for i in range(1, n + 1):
        edges = list(map(int, input(f"Enter neighbors of node {i} (space-separated): ").split()))
        graph[i] = edges

    start = int(input("Enter starting node for BFS: "))

    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("Breadth First Search traversal:")
    recursive_bfs(graph, queue, visited)

# Run the program
main()
