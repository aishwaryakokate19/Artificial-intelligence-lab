import heapq

# Function to build the graph from user input
def create_weighted_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    print("Enter each edge in the format: vertex1 vertex2 weight")
    for _ in range(num_edges):
        u, v, w = input().split()
        w = int(w)

        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Since it's undirected
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph

# Prim's Algorithm function
def prims_algorithm(graph, start_vertex):
    visited = set()
    min_heap = [(0, start_vertex, None)]  # (weight, current_vertex, previous_vertex)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)

        if current not in visited:
            visited.add(current)
            total_cost += weight

            if prev is not None:
                mst_edges.append((prev, current, weight))

            for neighbor, edge_weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return total_cost, mst_edges

# Main execution
if __name__ == "__main__":
    graph = create_weighted_graph()
    start_vertex = input("Enter the starting vertex for Prim's Algorithm: ")
    
    cost, mst = prims_algorithm(graph, start_vertex)

    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print(f"Total cost of MST: {cost}")
