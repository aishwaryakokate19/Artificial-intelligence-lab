# Disjoint Set Union (Union-Find) class
class DisjointSet:
    def __init__(self, vertices):  # Fixed __init__ method
        self.parent = {v: v for v in vertices}
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

# Function to read edges from user
def read_graph():
    edges = []
    vertices = set()
    num_edges = int(input("Enter the number of edges: "))

    print("Enter each edge in the format: vertex1 vertex2 weight")
    for _ in range(num_edges):
        u, v, w = input().split()
        w = int(w)
        edges.append((w, u, v))
        vertices.add(u)
        vertices.add(v)
    
    return list(vertices), edges

# Kruskal's Algorithm
def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    # Sort edges by weight
    edges.sort()

    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# Main
if __name__ == "__main__":  # Fixed __name__ block
    vertices, edges = read_graph()
    mst, cost = kruskal(vertices, edges)

    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print(f"Total cost of MST: {cost}")
