Ideias:

Redes Neurais:


- gerar população inicial usando redes neurais ou algum outro método que leve em consideração informações históricas tentando identificar padrões. (por exemplo: sempre nessa época do ano o lixo se acumula dessa forma específica).
- para gerar uma solução usando uma rede neural ela deveria gerar uma ordenação dos elementos

GRASP: 

- gerar população inicial usando o primeiro passo do GRASP
- e se eu encarar minha população toda como sendo um individuo. Cada geração do genético seria uma contrução do GRASP por exemplo e a busca local seria feita sobre esses individuos.

Modificações para o Genético Atual:

- talvez usar outras técnicas de seleção de indivíduos diferentes de truncation selection
- essa questão de crossover e mutation ratio é estranha.
- usar busca local no algoritmo genético
- latas de lixo mais cheias poderiam ter mais prioridade nas soluções
- mudar o cálculo do peso das arestas do grafo
- duplicar os individuos na selecao é benefico?
- mudar o calculo de fitness?
- talvez no iterated crossover usar somente uma vez um individuo para gerar prole
- ao invés de só duplicar os elementos depois da seleção usar algum tipo de heuristica para melhorar as soluções
- valor mais bem ajustado de mutação 
- testar outros métodos de crossing

ILS:

- sera que quando a condição de parada for alcançada pode-se perturbar a solução como no ILS para gerar uma nova população e tentar encontrar outro mínimo. E se o ILS não for sobre um único indivíduo mas sobre uma população inteira?

VND/VNS:

- usar busca local progressiva no algoritmo genético

Anotações:

genético + busca local (talvez do grasp)
citar que não consegui acesso à base de dados

Algoritmos que o professor expôs:

ILS: 

1. perturbing the current local minimum
2. applying local search after starting from the modified solution

VND

Conjunto de estruturas de vizinhança.
Explora o espaço de soluções através de trocas sistemáticas de estruturas de vizinhança
Explora vizinhanças de modo gradual.
Solução base pode ser um cromossomo gerado pelo genético.

VNS

Loop externo no VND. A cada iteração gera um vizinho qualquer da melhor solução do VNS

GRASP

GRASP é usualmente implementado como um procedimento "multi-start" onde a cada iteração, é feito uma etapa de construção e uma de busca local.
A construção é feita elemento a elemento. 
Seleciona uma lista restrita de melhores candidatos dentre todos os possíveis. Escolhe-se randômicamente um elemento dessa lista restrita.

Algoritmos genéticos -

Links:

https://www.dca.fee.unicamp.br/~gomide/courses/EA072/artigos/Genetic_Algorithm_TSPR_eview_Larranaga_1999.pdf

https://www.math.uwaterloo.ca/tsp/world/djlog.html

https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html

TODO:

Implementar modificações propostas no artigo
Ajeitar referências
Ajeitar identificadores das seções
Melhorar introdução 
Escrever abstract 
Adicionar seções que ele pediu
Escrever seção de experimentos
Escrever conclusão
Gravar video
Revisar artigo
Resolver comentários no artigo