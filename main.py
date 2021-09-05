graph = []

graph_file = open("graph.txt", "r")

for line in graph_file:
    graph.append([float(x) if x != 'INF' else 9999999 for x in line.replace('\n','').split(' ')])

def floydWarshall(adj_matrix):
    n_vertices = len(graph)

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])       

    return dist

dist = floydWarshall(graph)

print(dist)

# INPUT: The adjacency matrix of digraph with n vertices,
# where distances d are ranging from 0 to ∞
# OUTPUT: The transitive closure of the digraph
# for each vertex v
# d[v][v] ← 0
# for each edge (e, v)
# d[u][v] ← w(u,v)
# for k ← 1 to n do
# for i ← 1 to n do
# for j ← 1 to n do
# if d[i][j] > d[i][k] + d[k][j]
# d[i][j] ← d[i][k] + d[k][j]
# end if