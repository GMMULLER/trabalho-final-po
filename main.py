import random

best_individual = []

def twoOptimalSwap(ind,i,k):
    new_route = []

    for i in range(0,i):
        new_route.append(ind[i])
        print(new_route)

    for i in range(k,i,-1):
        new_route.append(ind[i])
        print(new_route)

    for i in range(k+1,len(ind)):
        new_route.append(ind[i])
        print(new_route)

    return new_route

# Gera todas as combinacoes do dois optimal
def twoOptimal(adj_matrix,ind):
    new_routes = [[ind[0].copy(),ind[1]]]

    for i in range(0,len(ind[0])):
        for k in range(i+1,len(ind[0])+1):
            new_route = twoOptimalSwap(ind[0],i,k)
            # new_fitness = fitness(adj_matrix,new_route)
            new_fitness = 0

            new_routes.append([new_route,new_fitness])

    return new_routes

print(twoOptimal([],[1,2,3,4]))

def sortCriteria(elem):
    return elem[1]

def fitness(adj_matrix, vetor):
    weight = 0
    for el_index in range(len(vetor)-1):
        weight += adj_matrix[vetor[el_index]][vetor[el_index+1]]

    weight += adj_matrix[vetor[-1]][vetor[0]]

    return weight

# Levando em consideracao que pode-se iniciar em qualquer no. E que a partir de qualquer noh eh possivel visitar qualquer outro
def generateInitialPopulation(adj_matrix, size):
    nodes = []
    population = []

    for i in range(len(adj_matrix)):
        nodes.append(i)

    for k in range(size):
        random.shuffle(nodes)
        
        weight = fitness(adj_matrix, nodes)
        
        population.append([nodes.copy(),weight])

    population.sort(key=sortCriteria)

    return population

def floydWarshall(adj_matrix):
    n_vertices = len(adj_matrix)

    dist = list(map(lambda i: list(map(lambda j: j, i)), adj_matrix))

    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])       

    return dist

def truncationSelection(population, x):
    original_size = len(population)
    percent_increment = 1/len(population)
    percentage = 0

    selected_population = []

    for solution in population:
        percentage += percent_increment

        selected_population.append([solution[0].copy(),solution[1]])

        if percentage >= x:
            break

    duplicate_index = 0
    original_size_selected_pop = len(selected_population)

    # "These fittest individuals are duplicated so the population size is maintained" 
    while(len(selected_population) < original_size):

        selected_population.append([selected_population[duplicate_index][0].copy(),selected_population[duplicate_index][1]])

        duplicate_index += 1

        if duplicate_index == original_size_selected_pop:
            duplicate_index = 0

    return selected_population

def breed(adj_matrix, parent1, parent2):
    child = [-1]*len(parent1)
    
    geneA = int(random.random() * (len(parent1)+1))
    geneB = int(random.random() * len(parent1))
    
    while(geneA == geneB):
        geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        child[i] = parent1[i]
    
    index_child = 0

    for elem in parent2:
        while(index_child >= startGene and index_child < endGene):
            index_child += 1

        if elem not in child:
            child[index_child] = elem
            index_child += 1

    weight = fitness(adj_matrix, child)

    return [child,weight]

# Esse crossover pode gerar individuos que nao sao uma solucao possivel, neh? (obs)
# Vou implementar o ordered crossover no lugar (obs)
def crossover(adj_matrix,population,percent):
    # # Parents
    # p1 = None
    # p2 = None

    # # E se nao achar dois pais que satisfacam o criterio? (obs)
    # for p1_candidate in population:
    #     for p2_candidate in population:
    #         if p1_candidate != p2_candidate and p1_candidate[n] == p2_candidate[n]:
    #             p1 = p1_candidate
    #             p2 = p2_candidate
    #             break

    # # Create empty road pc
    # pc = [[]]

    # # copy to beginning pc a part of road p1: p1{0..n}
    # for i in range(n):
    #     pc[0].append(p1[0][i])

    # # copy to end of pc a part of road p2: p2{n..end}
    # for i in range(n,len(p2)):
    #     pc[0].append(p2[0][i])

    # weight = 0
    # for el_index in range(len(pc)-1):
    #     weight += adj_matrix[pc[0][el_index]][pc[0][el_index+1]]
    
    # pc.append(weight)

    new_population = []

    while(len(new_population) < len(population)):

        parent1 = random.choice(population) 
        parent2 = random.choice(population)        

        while parent1 == parent2:
            parent2 = random.choice(population)

        if(random.random() <= percent):
            child = breed(adj_matrix,parent1[0],parent2[0])
            new_population.append(child)
        else:
            new_population.append([parent1[0].copy(),parent1[1]])

    return new_population

#min. de mutacao nao faz muito sentido (TODO)
def mutation(adj_matrix,population,percent):

    for elem in population:
        if(random.random() <= percent):
            
            swap1 = int(random.random() * len(elem[0]))
            swap2 = int(random.random() * len(elem[0]))

            while(swap2 == swap1):
                swap2 = int(random.random() * len(elem[0]))

            aux_swap = elem[0][swap1]
            elem[0][swap1] = elem[0][swap2]
            elem[0][swap2] = aux_swap

            elem[1] = fitness(adj_matrix,elem[0])

# graph = []

# # graph_file = open("graph.txt", "r")
# graph_file = open("att48_d_formated.txt", "r")

# for line in graph_file:
#     graph.append([float(x) if x != 'INF' else 99999999 for x in line.replace('\n','').split(' ')])

# complete_digraph = floydWarshall(graph)

# population = generateInitialPopulation(complete_digraph, 5000)

# # print("Initial population:")
# # for p in population:
# #     print(p)

# # debbug
# # for i in complete_digraph:
# #     print(i)

# # print("=============")

# print("=============")

# # criteria_fullfilled = False

# for i in range(500):
#     print("Iteracao i: "+str(i))

#     population.sort(key=sortCriteria)

#     # while(not criteria_fullfilled):
#     population = truncationSelection(population,0.6)
#     # print("Population after selection: ")
#     # for p in population:
#     #     print(p)

#     population = crossover(complete_digraph,population,0.2)

#     # print("Population after crossover: ")
#     # for p in population:
#     #     print(p)

#     # print("Population after mutation: ")
#     mutation(complete_digraph,population,0.8)

#     for elem in population:
#         if len(best_individual) == 0:
#             best_individual = [elem[0].copy(), elem[1]]
#         else:
#             if elem[1] < best_individual[1]:
#                 best_individual = [elem[0].copy(), elem[1]]

#     # for p in population:
#     #     print(p)

# print("Best individual: ")
# print(best_individual)