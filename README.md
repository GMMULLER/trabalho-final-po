- como melhorar o algoritmo
- gerar população inicial usando o primeiro passo do GRASP
- gerar população inicial usando redes neurais ou algum outro método que leve em consideração informações históricas tentando identificar padrões. (por exemplo: sempre nessa época do ano o lixo se acumula dessa forma específica).
- para gerar uma solução usando uma rede neural ela deveria gerar uma ordenação dos elementos
- talvez usar outras técnicas de seleção de indivíduos diferentes de truncation selection
- sera que quando a condição de parada for alcançada pode-se perturbar a solução como no ILS para gerar uma nova população e tentar encontrar outro mínimo. E se o ILS não for sobre um único indivíduo mas sobre uma população inteira?
- essa questão de crossover e mutation ratio é estranha.
- usar busca local no algoritmo genético 
- variar aplicação das buscas locais
- latas de lixo mais cheias poderiam ter mais prioridade nas soluções
- mudar o cálculo do peso das arestas do grafo


- each road (edge) has two parameters for both directions, which represent different weight of each direction i.e. one direction of the road is more loaded than other
- one-way road pode ser resentada colocando infinito em alguma das direções
- o peso é computado como uma soma de todos os parâmetros que impactam a rua, por exemplo: distância, traffic-density, road quality.
- dado um digrafo incompleto que mapeia as ruas e as latas de lixo da cidade usa Floyd Warshall para gerar um digrafo completo.
- TSP assimétrico
- Etapas:
    - Geração da população
    - Processo de seleção, recombinação (crossover) e mutação
    - Critério principal para escrolher o melhor indivíduo e a melhor solução     
- aparentemente a população inicial é gerada randomicamente
- O tipo de seleção usado é o truncation selection (retains the fittest x% of the population). Esses fittest são duplicados para manter o tamanho da população.
- O crossover é dado por um limite máximo de crossing (que também é o valor mínimo de mutação).
- The same individuals should not be crossed, but mutated to get better or new individual.
- Se uma nova solucao não é melhor que a anterior por b% por a iterações para. (Para não travar num máximo ou mínimo local).


    https://www.dca.fee.unicamp.br/~gomide/courses/EA072/artigos/Genetic_Algorithm_TSPR_eview_Larranaga_1999.pdf