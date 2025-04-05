def read_input(filename):
    file = open(filename, "r")
    line = file.readline()
    parts = line.split()
    n = int(parts[0])
    m = int(parts[1])
    k = int(parts[2])

    graph = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            row.append(0)
            j += 1
        graph.append(row)
        i += 1

    edge_count = 0
    while edge_count < m:
        line = file.readline()
        if line == "":
            break
        parts = line.split()
        if len(parts) < 2:
            continue

        u = int(parts[0])
        v = int(parts[1])
        graph[u][v] = 1
        graph[v][u] = 1
        edge_count += 1

    file.close()
    return n, k, graph

def is_safe(vertex, graph, colors, color):
    i = 0
    while i < len(graph):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
        i += 1
    return True

def graph_coloring_util(graph, k, colors, vertex, n):
    if vertex == n:
        return True

    color = 1
    while color <= k:
        if is_safe(vertex, graph, colors, color):
            colors[vertex] = color
            if graph_coloring_util(graph, k, colors, vertex + 1, n):
                return True
            colors[vertex] = 0
        color += 1

    return False

def graph_coloring(filename):
    n, k, graph = read_input(filename)

    colors = []
    i = 0
    while i < n:
        colors.append(0)
        i += 1

    if graph_coloring_util(graph, k, colors, 0, n):
        print("Coloring Possible with", k, "Colors")
        print("Color Assignment:", colors)
    else:
        print("Coloring Not Possible with", k, "Colors")

if __name__ == "__main__":
    graph_coloring("input.txt")
