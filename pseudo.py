# Code 1. XML parsing

# INPUT: SVG File with graph map
# OUTPUT: Graph coordinates, Weight road
# From SVG → load distance attribute dist;
# create vector[x][y];
# vector [x][y]= split(dist);
# load end of road → n
# x → consists direction of road nodes in order 0 to n;
# y → consists direction of road nodes in order n to 0;
# return dist, vector

# Code 2. Used Floyd-Warshall algorithm for graph processing

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

# Code 3. Used crossover algorithm

# INPUT: Random index n, where it will occur the crossing
# OUTPUT: The crossed individual (road) pc
# Choose two roads from population p1, p2, where p1[n] =
# p2[n]
# Create empty road pc
# Copy to beginning pc a part of road p1: p1{0..n}
# Copy to end of pc a part of road p2: p2{n..end}
# Compute the final weight of pc

# Code 4. Used Mutation algorithm

# INPUT: Random indexes i, j
# OUTPUT: The mutated individual (road) pm
# Choose one road from population p1
# Create empty road pm
# pm[i] = p1[j]
# pm[j] = p1[i]
# Compute the final weight of pm