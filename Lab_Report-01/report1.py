import random

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.moves = [(1, 0, "Moving Down"), (-1, 0, "Moving Up"), (0, 1, "Moving Right"), (0, -1, "Moving Left")]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.path = []
        self.topo_order = []

    def pos(self, graph):
        while True:
            x, y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if graph[x][y] == 1:
                return x, y

    def init(self):
        self.N = random.randint(4, 7)
        print(f"\nN = {self.N}")
        graph = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]

        print("\nGrid:")
        for row in graph:
            print("[", " ".join(map(str, row)), "]")

        source_x, source_y = self.pos(graph)
        goal_x, goal_y = self.pos(graph)

        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, float("inf"))

        print(f"\nSource: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})\n")

        visited = [[False] * self.N for _ in range(self.N)]
        self.path = []
        self.topo_order = []
        self.found = False

        print("DFS Moves:")
        self.st_dfs(graph, self.source, visited, [])

        if self.found:
            print("\nGoal found!")
            print("Number of Minimum Moves Required:", self.goal.depth)
            print("Topological Order of Node Traversal:", self.topo_order)
        else:
            print("\nGoal Cannot Be Reached.")

    def st_dfs(self, graph, u, visited, current_path):
        if self.found:
            return
        
        visited[u.x][u.y] = True
        current_path.append((u.x, u.y))
        self.topo_order.append((u.x, u.y))
        
        if u.x == self.goal.x and u.y == self.goal.y:
            self.found = True
            self.goal.depth = u.depth
            print("\nDFS PATH:")
            print(" → ".join([f"({x},{y})" for x, y in current_path]))
            return
        
        for dx, dy, direction in self.moves:
            v_x, v_y = u.x + dx, u.y + dy
            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1 and not visited[v_x][v_y]:
                print(f"{direction} → ({v_x},{v_y})")
                self.st_dfs(graph, Node(v_x, v_y, u.depth + 1), visited, current_path[:])
                if self.found:
                    return

        visited[u.x][u.y] = False


def main():
    d = DFS()
    d.init()

if __name__ == "__main__":
    main()
