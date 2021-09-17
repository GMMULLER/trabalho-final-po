from os import X_OK
import random

def twoOptimalSwap(ind,i,k):
    new_route = []

    for j in range(0,i):
        new_route.append(ind[j])

    for j in range(k,i-1,-1):
        new_route.append(ind[j])

    for j in range(k+1,len(ind)):
        new_route.append(ind[j])

    return new_route

def sortCriteria(elem):
    return elem[1]

def fitness(adj_matrix, vetor):
    weight = 0
    for el_index in range(len(vetor)-1):
        weight += adj_matrix[vetor[el_index]][vetor[el_index+1]]

    weight += adj_matrix[vetor[-1]][vetor[0]]

    return weight

# Gera todas as combinacoes do dois optimal
def twoOptimal(adj_matrix,ind):
    new_routes = [[ind[0].copy(),ind[1]]]
    best = []

    for i in range(0,len(ind[0])-1):
        for k in range(i+1,len(ind[0])):
            new_route = twoOptimalSwap(ind[0],i,k)
            new_fitness = fitness(adj_matrix,new_route)

            new_routes.append([new_route,new_fitness])

            if len(best) == 0:
                best = [new_route,new_fitness]
            else:
                if new_fitness < best[1]:
                    best = [new_route,new_fitness]

    return new_routes, best

# def vnsAfterSelection(adj_matrix,ind,i):    
#     s = ind

#     generated_ind = []
#     twoOptimalSet = []
    
#     while(len(generated_ind) < i):
#         k = 1
#         while k <= 1:
#             twoOptimalSet, s2 = twoOptimal(adj_matrix,s)
#             if s2[1] < s[1]:
#                 s = s2
#                 k = 1
#             else:
#                 k += 1

#         generated_ind.append([s[0].copy(),s[1]])
#         s = random.choice(twoOptimalSet)

#     return generated_ind

def vnsAfterSelection(adj_matrix,ind,i):    
    s = ind

    generated_ind = []
    twoOptimalSet = []
    
    while(len(generated_ind) < i):
        k = 1
        while k <= 1:
            twoOptimalSet, s2 = twoOptimal(adj_matrix,s)
            if s2[1] < s[1]:
                s = s2
                k = 1
            else:
                k += 1

        s = random.choice(twoOptimalSet)

        for elem in twoOptimalSet:
            generated_ind.append([elem[0].copy(),elem[1]])
            if len(generated_ind) >= i:
                break

    generated_ind.sort(key=sortCriteria)

    return generated_ind

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

def truncationSelection(adj_matrix, population, x):

    original_size = len(population)
    percent_increment = 1/len(population)
    percentage = 0

    selected_population = []

    for solution in population:
        percentage += percent_increment

        selected_population.append([solution[0].copy(),solution[1]])

        if percentage >= x:
            break

    i = original_size - len(selected_population)

    selected_population = selected_population + vnsAfterSelection(adj_matrix,population[0],i)

    return selected_population

def tournamentSelection(population):

    ind1 = random.choice(population)
    ind2 = random.choice(population)

    while ind1 == ind2:
        ind2 = random.choice(population)

    if ind1[1] < ind2[1]:
        return ind1
    else:
        return ind2

def hybridSelection(adj_matrix, percent, population):
    original_size = len(population)
    percent_increment = 1/len(population)
    percentage = 0
    
    selected_population = []

    while percentage < percent:
        percentage += percent_increment

        ind = tournamentSelection(population)

        selected_population.append([ind[0].copy(),ind[1]])

    i = original_size - len(selected_population)

    selected_population = selected_population + vnsAfterSelection(adj_matrix,population[0],i)

    return selected_population

def greedConstruction(adj_matrix):
    num_nodes = len(adj_matrix)
    solution = []

    current_node = int(random.random() * num_nodes)

    solution.append(current_node)

    while(len(solution) < num_nodes):
        next_jumps = adj_matrix[current_node].copy()

        next_jumps_array = []

        for i in range(len(next_jumps)):
            next_jumps_array.append([i,next_jumps[i]])

        next_jumps_array.sort(key=sortCriteria)

        for elem in next_jumps_array:
            if elem[0] not in solution:
                current_node = elem[0]
                solution.append(elem[0])
                break

    return [solution,fitness(adj_matrix,solution)]

def vnsInitialPopulation(adj_matrix, size):

    greedSolution = greedConstruction(adj_matrix)

    return vnsAfterSelection(adj_matrix,greedSolution,size)

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

def crossover(adj_matrix,population,original_size,percent):

    new_population = []

    while(len(new_population) < original_size):

        parent1 = random.choice(population) 
        parent2 = random.choice(population)        

        if parent1 == parent2:
            for elem in population:
                if elem != parent1:
                    parent2 = elem
                    break

        if(random.random() <= percent):
            child = breed(adj_matrix,parent1[0],parent2[0])
            # if child != parent1 and child != parent2 and child not in new_population:
            new_population.append(child)
        else:
            # if parent1 not in new_population:
            new_population.append([parent1[0].copy(),parent1[1]])
            # elif parent2 not in new_population:
                # new_population.append([parent2[0].copy(),parent2[1]])
    
    return new_population

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

graph = []

# graph_file = open("graph.txt", "r")
graph_file = open("att48_d_formated.txt", "r")

for line in graph_file:
    graph.append([float(x) if x != 'INF' else 99999999 for x in line.replace('\n','').split(' ')])

complete_digraph = floydWarshall(graph)

population_size = 5000

population = vnsInitialPopulation(complete_digraph, population_size)

# print("Initial population:")
# for p in population:
#     print(p)

# debbug
# for i in complete_digraph:
#     print(i)

best_individual = []
generations_without_improvement = 0
total_iterations = 0
minimum_improvement = 0.005

while(True):
    print("Iteracao i: "+str(total_iterations))

    population = hybridSelection(complete_digraph,0.9,population)
    # print("Population after selection: ")
    # for p in population:
    #     print(p)

    population = crossover(complete_digraph,population,population_size,0.3)

    # print("Population after crossover: ")
    # for p in population:
    #     print(p)

    # print("Population after mutation: ")
    mutation(complete_digraph,population,0.25)

    population.sort(key=sortCriteria)

    total_iterations += 1 

    best_elem = population[0]

    improvement = minimum_improvement

    if len(best_individual) != 0:
        improvement = ((best_elem[1]/best_individual[1])-1)*-1

    if len(best_individual) != 0:
        print("Improvement: "+str(improvement)+" Best Solution: "+str(best_individual[1])+" Best Elem: "+str(best_elem[1]))

    if len(best_individual) == 0:
        best_individual = [best_elem[0].copy(), best_elem[1]]
    else:
        if best_elem[1] < best_individual[1]:
            best_individual = [best_elem[0].copy(), best_elem[1]]

    if improvement < minimum_improvement:
        generations_without_improvement += 1
    else:
        generations_without_improvement = 0

    if generations_without_improvement == 100:
        break

    # for p in population:
    #     print(p)

print("Best individual: ")
print(best_individual)
print("Iterações: ")
print(total_iterations)