# Portfólio: Resolvendo Problemas por Busca em Inteligência Artificial

## 1. Introdução: Importância e Impacto da Resolução de Problemas por Busca na IA e na Sociedade

A Inteligência Artificial (IA) envolve o estudo de agentes que recebem percepções do ambiente e realizam ações. Definimos IA como o estudo da ação racional e, nesse contexto, o planejamento — elaborar um plano de ação para alcançar objetivos — é uma parte crucial da IA.

A resolução de problemas por busca é uma técnica central em IA para encontrar uma sequência de ações que leve um agente a atingir um objetivo. Newell e Simon argumentaram que esta é a base essencial da resolução de problemas humanos, como um jogador de xadrez examinando movimentos ou um médico considerando diagnósticos alternativos. Embora as primeiras abordagens pudessem ser ineficientes sem orientação adequada, a busca, juntamente com a representação do conhecimento, permanece no cerne da maioria dos trabalhos modernos em IA.

A busca é uma metodologia de resolução de problemas que explora sistematicamente um espaço de estados, que representa os estágios sucessivos e alternativos no processo de busca pela solução. Exemplos práticos de aplicação da busca incluem layout VLSI (circuitos integrados de larga escala), navegação robótica, sequenciamento de montagem automática e problemas de roteamento. Além disso, a busca tem sido aplicada em áreas como diagnóstico de falhas mecânicas e mesmo no raciocínio baseado em lógica.

A capacidade de um agente de resolver problemas através da busca permite que ele navegue por ambientes complexos, tome decisões sequenciais e encontre caminhos para atingir metas, tornando-se uma ferramenta indispensável para a criação de sistemas inteligentes.

## 2. Apresentação dos Conceitos Principais

A abordagem de resolução de problemas por busca se baseia na ideia de que um agente pode adotar um objetivo e trabalhar para satisfazê-lo. Um agente de solução de problemas é um tipo de agente baseado em objetivos.

Os principais conceitos envolvidos são:

*   **Formulaçāo de Objetivo:** O agente adota um ou mais objetivos que deseja alcançar.
*   **Formulaçāo de Problema:** O agente descreve os estados possíveis do "mundo" e as ações que pode realizar para transitar entre esses estados, visando atingir o objetivo. Estados do mundo podem ser considerados como totalidades sem estrutura interna visível (representação atômica), que é a representação considerada na busca básica.
*   **Espaço de Estados (State Space):** É uma representação formal do problema. É definido por uma quádrupla `[N, A, S, GD]`, onde:
    *   `N` é o conjunto de nós ou estados do grafo, correspondendo aos estados no processo de resolução do problema.
    *   `A` é o conjunto de arcos que conectam pares de nós, representando conexões diretas ou ações que levam de um estado a outro.
    *   `S` é o estado inicial.
    *   `GD` é a descrição dos estados objetivo, ou seja, a condição que define que o problema foi resolvido.
    Uma solução para um problema é representada como um caminho no grafo do estado inicial a um estado objetivo.
*   **Busca (Search):** Antes de agir, o agente simula sequências de ações em seu modelo (o espaço de estados) para encontrar um caminho que leve ao objetivo. Isso envolve testar sistematicamente caminhos alternativos.
*   **Execução:** Uma vez encontrado um caminho (solução) pela busca, o agente executa as ações correspondentes no ambiente real.
*   **Agentes de Solução de Problemas:** São agentes baseados em objetivos que utilizam a busca em representações atômicas de estados para encontrar soluções.
*   **Estratégias de Busca:** São os algoritmos usados para explorar o espaço de estados. Elas podem ser:
    *   **Busca Cega (Uninformed Search):** Algoritmos que não utilizam nenhuma informação sobre o quão próximo um estado está do(s) objetivo(s) além da definição do problema.
    *   **Busca Informada (Informed Search):** Algoritmos que utilizam dicas específicas do domínio (heurísticas) sobre a localização dos objetivos para guiar a busca de forma mais eficiente.
*   **Heurísticas:** São funções, denotadas como `h(n)`, que fornecem uma estimativa do custo do caminho mais econômico do estado no nó `n` para um estado objetivo. Elas são informações específicas do domínio que podem melhorar significativamente a eficiência da busca.
*   **Medidas de Performance:** Critérios para avaliar algoritmos de busca:
    *   **Completude (Completeness):** O algoritmo garante encontrar uma solução quando existe uma, ou reportar a falha corretamente.
    *   **Otimização de Custos (Cost Optimization):** O algoritmo garante encontrar a solução com o menor custo.
    *   **Complexidade de Tempo (Time Complexity):** Quanto tempo leva para encontrar a solução.
    *   **Complexidade de Espaço (Space Complexity):** Quanta memória é necessária para a busca.
*   **Filas:** Estruturas de dados usadas para gerenciar a ordem em que os nós são explorados pelos algoritmos de busca: fila FIFO (First-In, First-Out) para busca em largura, pilha LIFO (Last-In, First-Out) para busca em profundidade, e fila de prioridade para busca *best-first*. O uso dessas estruturas permite que os algoritmos explorem estados não testados (lista *open*) e evitem repetir caminhos infrutíferos (lista *closed*).

# Análise de Algoritmos para Portfólio 2 de IA (Baseado em Russell & Norvig)



## 1. Algoritmos de Busca Cega (Uninformed Search)

Os algoritmos de busca cega, também conhecidos como busca não informada, exploram o espaço de estados sem utilizar qualquer conhecimento específico sobre a proximidade de um estado ao objetivo, baseando-se unicamente na estrutura do problema. Conforme apresentado por Russell e Norvig (2013), as principais estratégias dentro desta categoria incluem:

*   **Busca em Largura (Breadth-First Search - BFS):** Expande sistematicamente os nós mais rasos e não expandidos primeiro. Garante encontrar a solução mais rasa (ótima em termos de número de passos se os custos forem uniformes), mas pode exigir muita memória.
*   **Busca de Custo Uniforme (Uniform-Cost Search - UCS):** Expande o nó não expandido com o menor custo de caminho acumulado (`g(n)`). É ótima e completa, desde que os custos dos passos sejam não negativos. É essencialmente uma generalização da BFS para custos de passo variáveis.
*   **Busca em Profundidade (Depth-First Search - DFS):** Expande sempre o nó mais profundo na fronteira da árvore de busca. Usa menos memória que a BFS (ordem linear em relação à profundidade máxima), mas não é completa (pode se perder em caminhos infinitos) nem ótima por si só.
*   **Busca com Aprofundamento Iterativo (Iterative Deepening Depth-First Search - IDDFS ou IDS):** Combina os benefícios da BFS (completude e otimalidade para custos uniformes) e da DFS (requisitos modestos de memória). Realiza buscas em profundidade com limites de profundidade crescentes (1, 2, 3, ...), até encontrar a solução. Embora pareça redundante por repetir expansões, é geralmente o método de busca cega preferido quando o espaço de busca é grande e a profundidade da solução é desconhecida.
*   **Busca Bidirecional (Bidirectional Search):** Executa duas buscas simultâneas, uma partindo do estado inicial e outra partindo do estado objetivo (se as ações forem reversíveis), parando quando as duas buscas se encontram no meio. Pode reduzir drasticamente a complexidade de tempo e espaço, explorando uma área muito menor do espaço de estados em comparação com buscas unidirecionais.

*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 3.

---



## 2. Algoritmos de Busca Informada (Heurística)

Os algoritmos de busca informada, ou busca heurística, utilizam conhecimento específico do problema, na forma de uma função heurística `h(n)`, para estimar a distância (ou custo) de um estado `n` até o objetivo. Essa informação guia a busca de forma mais eficiente, priorizando caminhos que parecem mais promissores. Russell e Norvig (2013) destacam as seguintes abordagens:

*   **Busca Best-First Genérica (Generic Best-First Search):** É um paradigma de busca que seleciona o próximo nó a ser expandido com base em uma função de avaliação `f(n)`. Diferentes algoritmos best-first surgem da escolha de diferentes funções `f`.
*   **Busca Best-First Gulosa (Greedy Best-First Search):** Uma instância da busca best-first que tenta expandir o nó que está estimado como o mais próximo do objetivo, usando a função heurística diretamente como função de avaliação: `f(n) = h(n)`. Embora possa ser rápida, não é ótima nem completa.
*   **Busca A* (A* Search):** Considerado o algoritmo de busca heurística mais conhecido, A* combina o custo do caminho percorrido desde o início (`g(n)`) com a estimativa heurística do custo restante até o objetivo (`h(n)`), utilizando a função de avaliação `f(n) = g(n) + h(n)`. A* é completo e ótimo, desde que a heurística `h(n)` seja admissível (nunca superestima o custo real) e, para eficiência ótima, consistente. É amplamente utilizado em problemas de planejamento de caminhos e outros.
*   **Buscas Heurísticas com Memória Limitada:** Como A* pode consumir muita memória, foram desenvolvidas variantes que operam com restrições de espaço:
    *   **Busca Recursiva Best-First (Recursive Best-First Search - RBFS):** Simula a operação de A* usando apenas espaço linear. Faz isso explorando um caminho e mantendo o valor `f` do melhor caminho alternativo a partir de seus ancestrais. Se o custo do caminho atual exceder esse valor limite, ele retrocede e explora o caminho alternativo. Pode sofrer de recomputação excessiva.
    *   **SMA* (Simplified Memory-Bounded A*):** Utiliza toda a memória disponível. Expande os melhores nós folha até que a memória esteja cheia. Nesse ponto, remove o nó folha com o maior valor `f` (o pior) para liberar espaço para um novo nó. É completo se houver memória suficiente para armazenar o caminho da solução mais rasa e ótimo se encontrar uma solução.
*   **Aprendizado de Heurísticas (Learning Heuristics):** Abordagens onde a função heurística não é dada a priori, mas aprendida a partir da experiência ou de exemplos do problema, como resolver subproblemas mais simples (bases de dados de padrões) ou através de aprendizado indutivo.

*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 3.

---



## 3. Algoritmos de Busca em Ambientes Complexos

Ambientes complexos apresentam desafios adicionais em relação à busca clássica, como a necessidade de otimizar uma função objetivo sem se preocupar com o caminho, lidar com múltiplos agentes com objetivos conflitantes, agir sob incerteza ou com informações parciais. Russell e Norvig (2013) abordam diversas técnicas para esses cenários:

*   **Busca Local (Local Search):** Utilizada principalmente em problemas de otimização, onde o objetivo é encontrar o estado com o melhor valor de uma função objetivo, e o caminho até ele não importa. Esses algoritmos mantêm apenas um estado atual (ou um pequeno conjunto) e tentam melhorá-lo movendo-se para estados vizinhos.
    *   *Subida de Encosta (Hill Climbing):* Move-se continuamente em direção a um valor crescente da função objetivo. É simples e eficiente em memória, mas suscetível a máximos locais, platôs e cumeeiras.
    *   *Subida de Encosta com Reinício Aleatório (Random-Restart Hill Climbing):* Executa a subida de encosta múltiplas vezes a partir de estados iniciais aleatórios para aumentar a chance de encontrar o ótimo global.
    *   *Recozimento Simulado (Simulated Annealing):* Permite movimentos para estados piores com uma probabilidade que diminui ao longo do tempo (controlada por uma "temperatura"), ajudando a escapar de máximos locais.
    *   *Busca de Feixe Local (Local Beam Search):* Mantém `k` estados em paralelo. Em cada passo, gera todos os sucessores dos `k` estados e seleciona os `k` melhores sucessores para a próxima iteração. É menos suscetível a máximos locais que a subida de encosta simples.
    *   *Busca de Feixe Local Estocástica (Stochastic Beam Search):* Similar à busca de feixe local, mas escolhe os `k` sucessores com probabilidade proporcional à sua qualidade, introduzindo aleatoriedade.
*   **Busca Adversária (Adversarial Search - Jogos):** Projetada para ambientes competitivos com dois ou mais agentes (jogadores) com objetivos opostos. O objetivo é encontrar a melhor estratégia (sequência de movimentos) considerando as possíveis respostas do adversário.
    *   *Algoritmo Minimax:* Para jogos de soma zero com informação perfeita, calcula o movimento ótimo assumindo que o adversário também jogará otimamente para minimizar a utilidade do jogador.
    *   *Poda Alfa-Beta (Alpha-Beta Pruning):* Otimização do Minimax que descarta ramos da árvore de busca que não influenciarão a decisão final, reduzindo drasticamente o número de nós a serem explorados.
    *   *Funções de Avaliação Heurística:* Usadas em jogos complexos (como xadrez) onde a árvore completa é intratável. Estimam a utilidade esperada de um estado sem explorar até o final do jogo.
    *   *Busca em Árvore Monte Carlo (Monte Carlo Tree Search - MCTS):* Abordagem probabilística que equilibra exploração e explotação, realizando simulações aleatórias (playouts) a partir do estado atual para estimar o valor dos movimentos. Muito eficaz em jogos como Go.
*   **Busca Online (Online Search):** Aplicada quando o agente precisa agir em um ambiente antes de conhecer completamente o espaço de estados ou os resultados das ações. O agente intercala computação (planejamento) e execução, aprendendo sobre o ambiente à medida que se move.
    *   *Agentes de Busca Online:* Precisam tomar decisões com informações limitadas, explorando o ambiente e atualizando seu conhecimento.
    *   *LRTA* (Learning Real-Time A*):* Um exemplo de algoritmo de busca online que aprende custos heurísticos à medida que explora o ambiente.
*   **Busca com Ações Não Determinísticas ou Observações Parciais:** Lida com incerteza nos resultados das ações ou na percepção do estado atual.
    *   *Busca AND-OR:* Utilizada para encontrar planos de contingência que funcionam independentemente do resultado de ações não determinísticas.
    *   *Busca no Espaço de Crenças (Belief State Search):* Quando o ambiente é parcialmente observável, o agente mantém um estado de crença (uma distribuição de probabilidade sobre os estados possíveis) e busca no espaço desses estados de crença. Relevante para POMDPs (Processos de Decisão de Markov Parcialmente Observáveis).

*Referências:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulos 4 (Busca Local, Otimização), 5 (Busca Adversária), partes dos Capítulos 4 e 12 (Busca Online, Incerteza).

---



## 4. Algoritmos Genéticos e Evolucionários

Os Algoritmos Genéticos (AGs) pertencem a uma classe mais ampla de algoritmos evolucionários, que se inspiram na evolução biológica para resolver problemas de busca e otimização. Eles operam sobre uma população de soluções candidatas, aplicando operadores como seleção, recombinação (cruzamento) e mutação para gerar novas populações com aptidão progressivamente maior. Russell e Norvig (2013) discutem essas abordagens no contexto da busca local estocástica e otimização:

*   **Algoritmos Genéticos (Genetic Algorithms - GAs):** Os AGs mantêm uma população de estados candidatos (representados como strings ou cromossomos) e geram a próxima geração combinando pares de indivíduos (cruzamento) e introduzindo pequenas alterações aleatórias (mutação). A seleção dos pais geralmente favorece indivíduos com maior aptidão (fitness), que mede a qualidade da solução representada pelo indivíduo.
*   **Programação Genética (Genetic Programming - GP):** Uma variante dos AGs onde os indivíduos na população são programas de computador (geralmente representados como árvores de expressão) em vez de strings. O objetivo é evoluir um programa que resolva uma tarefa específica. Os operadores de cruzamento e mutação são adaptados para manipular essas estruturas de programa.
*   **Estratégias de Evolução (Evolution Strategies - ES):** Outra abordagem evolucionária, frequentemente usada para otimização de parâmetros em espaços contínuos. Diferentemente dos AGs clássicos que operam em representações binárias ou discretas e enfatizam o cruzamento, as ES geralmente trabalham com vetores de números reais e focam mais na mutação (frequentemente usando distribuições gaussianas) e na seleção determinística ou probabilística dos melhores indivíduos (pais e/ou filhos) para formar a próxima geração.

Esses algoritmos são considerados "disruptivos" ou estocásticos porque introduzem aleatoriedade e operam em populações, permitindo-lhes explorar diferentes regiões do espaço de busca simultaneamente e escapar de ótimos locais onde algoritmos mais determinísticos como a subida de encosta poderiam ficar presos.

*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 4 (particularmente a seção sobre algoritmos genéticos).

<!-- comentário 
## 5. Sugestões de Algoritmos Alternativos

Considerando os algoritmos já presentes em seu portfólio (BFS, A*, Hill Climbing e GA) e a lista de algoritmos disponíveis em Russell e Norvig (2013), sugiro as seguintes alternativas interessantes para cada categoria, que provavelmente diferem dos exemplos dados em sala:

*   **Para Busca Cega:** Em vez de BFS, sugiro a **Busca com Aprofundamento Iterativo (Iterative Deepening Depth-First Search - IDDFS)**. Este algoritmo combina a completude e otimalidade (para custos uniformes) da BFS com a eficiência de memória da DFS, sendo uma escolha robusta quando a profundidade da solução é desconhecida.
*   **Para Busca Informada:** Como alternativa ao A*, proponho a **Busca Recursiva Best-First (Recursive Best-First Search - RBFS)**. Ela tenta emular a A* usando espaço de memória linear, o que a torna útil em problemas onde a memória é uma restrição significativa, embora possa recomputar nós.
*   **Para Busca em Ambientes Complexos:** No lugar da Subida de Encosta, sugiro o **Recozimento Simulado (Simulated Annealing)**. É um algoritmo de busca local estocástico que permite movimentos para estados piores com uma probabilidade decrescente, o que o ajuda a escapar de ótimos locais onde a Subida de Encosta poderia ficar presa.
*   **Para Algoritmos Genéticos/Disruptivos:** Como alternativa ao Algoritmo Genético clássico, sugiro as **Estratégias de Evolução (Evolution Strategies - ES)**. Embora compartilhem a inspiração evolucionária, as ES frequentemente operam em espaços contínuos e utilizam mecanismos de mutação e seleção distintos dos AGs tradicionais, focando mais na otimização de parâmetros.

A seguir, apresentarei uma explicação detalhada para cada um desses algoritmos selecionados.

---
-->



### 5.1. Busca Cega Alternativa: Busca com Aprofundamento Iterativo (IDDFS)

A Busca com Aprofundamento Iterativo (Iterative Deepening Depth-First Search - IDDFS), conforme descrita por Russell e Norvig (2013), representa uma engenhosa combinação das vantagens da Busca em Largura (BFS) e da Busca em Profundidade (DFS). Enquanto a BFS garante encontrar a solução mais rasa (ótima em termos de número de passos para custos uniformes) e é completa, ela sofre com altos requisitos de memória, que podem crescer exponencialmente com a profundidade. Por outro lado, a DFS possui requisitos de memória modestos (lineares em relação à profundidade máxima), mas não é completa em espaços de estados infinitos ou com ciclos, e não garante otimalidade.

A IDDFS supera essas limitações realizando repetidas buscas em profundidade, mas com um limite de profundidade crescente. Ela começa com uma busca em profundidade limitada à profundidade 0 (apenas o nó inicial). Se a solução não for encontrada, ela descarta os nós gerados e inicia uma nova busca em profundidade, desta vez com limite 1. Esse processo continua, incrementando o limite de profundidade (2, 3, 4, ...) a cada iteração, até que uma solução seja encontrada no limite de profundidade atual `d`. Como ela explora todos os nós até a profundidade `d-1` antes de explorar qualquer nó na profundidade `d`, ela efetivamente simula a ordem de expansão da BFS, garantindo que a primeira solução encontrada seja a mais rasa (e, portanto, ótima se os custos dos passos forem uniformes).

A principal preocupação com a IDDFS é a aparente redundância, já que os nós nos níveis superiores da árvore de busca são gerados múltiplas vezes em diferentes iterações. No entanto, Russell e Norvig (2013) demonstram que, para árvores de busca onde a maioria dos nós está no nível mais baixo (o que é comum em muitos problemas, especialmente com fatores de ramificação maiores que 1), o custo adicional de regenerar os nós superiores é relativamente pequeno em comparação com o custo de explorar o último nível. A complexidade de tempo da IDDFS acaba sendo da mesma ordem de magnitude que a da BFS (O(b^d)), enquanto sua complexidade de espaço é a mesma da DFS (O(bd)), onde `b` é o fator de ramificação e `d` é a profundidade da solução mais rasa. Essa combinação de completude, otimalidade (para custos uniformes) e eficiência de memória torna a IDDFS a estratégia de busca cega preferida em muitas situações onde o espaço de estados é grande e a profundidade da solução é desconhecida.

```python


# Representação de um grafo simples como dicionário

grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['F'],
    'E': [],
    'F': []
}

def dfs_limitado(grafo, no_atual, objetivo, limite):
    """
    Busca em profundidade limitada a um certo nível.
    
    :param grafo: Dicionário representando o grafo
    :param no_atual: Nó atual na busca
    :param objetivo: Nó que queremos encontrar
    :param limite: Profundidade máxima permitida
    :return: True se o objetivo for encontrado, False caso contrário
    """
    print(f"Visitando {no_atual}, limite restante: {limite}")
    
    if no_atual == objetivo:
        return True
    if limite == 0:
        return False

    for vizinho in grafo.get(no_atual, []):
        if dfs_limitado(grafo, vizinho, objetivo, limite - 1):
            return True
    return False

def iddfs(grafo, inicio, objetivo, limite_maximo):
    """
    Busca com Aprofundamento Iterativo (IDDFS).
    
    :param grafo: Dicionário com os nós e vizinhos
    :param inicio: Nó inicial da busca
    :param objetivo: Nó que queremos encontrar
    :param limite_maximo: Profundidade máxima de busca
    :return: True se encontrou o objetivo, False caso contrário
    """
    for profundidade in range(limite_maximo + 1):
        print(f"\n🔁 Profundidade atual: {profundidade}")
        if dfs_limitado(grafo, inicio, objetivo, profundidade):
            print(f"\n✅ Objetivo '{objetivo}' encontrado na profundidade {profundidade}.")
            return True
    print(f"\n❌ Objetivo '{objetivo}' não encontrado até a profundidade {limite_maximo}.")
    return False

# Executa o algoritmo procurando o nó 'F' a partir do nó 'A' com profundidade máxima 3
iddfs(grafo, 'A', 'F', 3)
```


*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 3.

---



### 5.2. Busca Informada Alternativa: Busca Recursiva Best-First (RBFS)

A Busca A* é renomada por sua otimalidade e completude quando usada com heurísticas admissíveis, mas sua principal desvantagem reside na potencial necessidade exponencial de memória para armazenar a fronteira (nós abertos). Para contornar essa limitação, Russell e Norvig (2013) apresentam a Busca Recursiva Best-First (Recursive Best-First Search - RBFS), um algoritmo que visa mimetizar a operação da A* utilizando apenas espaço linear, similar à busca em profundidade.

A RBFS opera de forma recursiva. Ela mantém o controle do valor `f` (custo `g` + heurística `h`) do melhor caminho alternativo disponível a partir do ancestral do nó atual (um limite superior, `f_limit`). A função recursiva explora um caminho enquanto o valor `f` dos nós nesse caminho não excede esse limite. Se um nó folha é alcançado e representa uma solução, a busca termina com sucesso. Se todos os caminhos a partir de um nó excedem o `f_limit`, a recursão retrocede (backtracks) para o nó ancestral. Crucialmente, ao retroceder, a RBFS atualiza o valor `f` do nó que acabou de explorar para refletir o melhor valor `f` encontrado em seus descendentes (incluindo aqueles que excederam o limite). Esse valor atualizado pode então guiar a busca futura, potencialmente fazendo com que a RBFS decida explorar um caminho diferente que antes parecia menos promissor, mas cujo valor `f` agora é o melhor abaixo do limite.

A principal vantagem da RBFS é sua eficiência de espaço, que é linear em relação à profundidade da solução mais rasa (`O(bd)`). Ela também é ótima e completa, assim como A*, *se* conseguir encontrar a solução (o que depende de ter memória suficiente para o caminho em si e a pilha de recursão). No entanto, sua maior desvantagem é a potencial re-geração excessiva de nós. Como ela descarta subárvores ao retroceder para economizar memória, pode ser que precise re-explorar a mesma subárvore múltiplas vezes se os limites `f` mudarem favoravelmente para ela novamente. Esse comportamento pode tornar a RBFS significativamente mais lenta que a A* em termos de tempo, especialmente se os valores `f` dos nós forem muito próximos entre si, levando a muitas mudanças de foco entre diferentes caminhos. Apesar disso, a RBFS é uma alternativa valiosa quando a memória é o principal gargalo para a aplicação da A*.

```python
import math

# Representação do grafo com custos reais (g) e heurísticas (h)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heurística h(n) estimando a distância de n até o objetivo G
heuristica = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 7,
    'E': 4,
    'F': 2,
    'G': 0  # objetivo
}

def rbfs(no, objetivo, g, f_limit):
    """
    Implementa a Busca Recursiva Best-First Search (RBFS).
    
    :param no: Nó atual
    :param objetivo: Nó alvo
    :param g: Custo acumulado até aqui
    :param f_limit: Limite superior de f(n) aceito até o momento
    :return: (solução encontrada?, novo f(n) mínimo entre as opções seguintes)
    """
    print(f"🔍 Explorando {no} com f_limit={f_limit}")

    if no == objetivo:
        print(f"✅ Objetivo {objetivo} alcançado!")
        return True, g + heuristica[no]

    # Gerar sucessores com seus valores f(n) = g + custo + h
    sucessores = []
    for vizinho, custo in grafo.get(no, []):
        f_n = g + custo + heuristica[vizinho]
        sucessores.append((vizinho, g + custo, f_n))

    if not sucessores:
        return False, math.inf  # sem sucessores = caminho morto

    while True:
        # Ordenar sucessores pelo menor f(n)
        sucessores.sort(key=lambda x: x[2])
        melhor = sucessores[0]
        print(f"➡️ Melhor: {melhor[0]} com f={melhor[2]}")

        if melhor[2] > f_limit:
            return False, melhor[2]  # excede o limite permitido

        # Escolha alternativa mais promissora caso a atual falhe
        alternativa = sucessores[1][2] if len(sucessores) > 1 else math.inf
        resultado, novo_f = rbfs(melhor[0], objetivo, melhor[1], min(f_limit, alternativa))
        sucessores[0] = (melhor[0], melhor[1], novo_f)

        if resultado:
            return True, novo_f

def iniciar_rbfs(inicio, objetivo):
    print(f"🚀 Iniciando RBFS de {inicio} até {objetivo}")
    sucesso, _ = rbfs(inicio, objetivo, 0, math.inf)
    if sucesso:
        print("🏁 Caminho encontrado com sucesso!")
    else:
        print("❌ Caminho não encontrado.")



```



*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 3.

---



### 5.3. Busca em Ambientes Complexos Alternativa: Recozimento Simulado (Simulated Annealing)

Enquanto a Subida de Encosta (Hill Climbing) é uma técnica de busca local direta que sempre busca melhorias imediatas, ela frequentemente falha ao ficar presa em ótimos locais. O Recozimento Simulado (Simulated Annealing), apresentado por Russell e Norvig (2013) como uma melhoria sobre a subida de encosta, oferece uma solução probabilística para este problema. Inspirado no processo físico de recozimento (annealing) em metalurgia, onde um material é aquecido e depois resfriado lentamente para aumentar o tamanho de seus cristais e reduzir seus defeitos, o algoritmo permite movimentos ocasionais para estados piores, diminuindo a probabilidade desses movimentos ao longo do tempo.

O algoritmo começa em um estado inicial aleatório e, a cada iteração, considera um movimento para um vizinho aleatório. Se o vizinho for melhor (maior valor na função objetivo para maximização, ou menor para minimização), o movimento é sempre aceito. Se o vizinho for pior, ele ainda pode ser aceito com uma certa probabilidade, que depende de dois fatores: quão pior é o vizinho (a diferença de valor, `ΔE`) e um parâmetro chamado "temperatura" (`T`). A probabilidade de aceitar um movimento pior é tipicamente dada por `exp(ΔE / T)` (para maximização, onde `ΔE` seria negativo e menor; para minimização, seria `exp(-ΔE / T)` com `ΔE` positivo). No início, a temperatura `T` é alta, permitindo que muitos movimentos ruins sejam aceitos, o que possibilita ao algoritmo explorar amplamente o espaço de busca e escapar de ótimos locais iniciais. Gradualmente, a temperatura é reduzida de acordo com um "cronograma de resfriamento" (cooling schedule). À medida que `T` diminui, a probabilidade de aceitar movimentos ruins também diminui, fazendo com que o algoritmo se concentre cada vez mais em melhorias locais, convergindo eventualmente para um estado de baixa energia (alta qualidade).

A grande vantagem do Recozimento Simulado é sua capacidade de encontrar ótimos globais (ou soluções muito próximas a eles) com maior probabilidade do que a Subida de Encosta, justamente por permitir escapar de ótimos locais. No entanto, seu desempenho é muito sensível à escolha do cronograma de resfriamento (como a temperatura inicial, a taxa de decaimento e o critério de parada). Um resfriamento muito rápido pode fazer com que ele se comporte como a Subida de Encosta e fique preso; um resfriamento muito lento pode torná-lo computacionalmente caro. Apesar dessa necessidade de ajuste de parâmetros, o Recozimento Simulado é uma técnica robusta e amplamente utilizada para problemas de otimização combinatória complexos, como o problema do caixeiro viajante, projeto de circuitos e alocação de recursos.

```python


import math
import random

# Função objetivo que queremos maximizar
def funcao_objetivo(x):
    return x * math.sin(x)

# Gera um novo vizinho com uma pequena perturbação
def vizinho(x, intervalo=0.5):
    return x + random.uniform(-intervalo, intervalo)

# Cronograma de resfriamento simples: temperatura decai lentamente
def simulated_annealing():
    # Parâmetros iniciais
    temperatura_inicial = 1000
    temperatura_final = 1e-3
    fator_resfriamento = 0.95
    max_iter_por_temp = 100

    # Estado inicial aleatório dentro do intervalo [0, 10]
    estado_atual = random.uniform(0, 10)
    valor_atual = funcao_objetivo(estado_atual)

    temperatura = temperatura_inicial

    print(f"🚀 Início: x = {estado_atual:.4f}, f(x) = {valor_atual:.4f}")

    while temperatura > temperatura_final:
        for _ in range(max_iter_por_temp):
            candidato = vizinho(estado_atual)
            # Garantir que o candidato continue dentro do intervalo
            candidato = max(0, min(10, candidato))

            valor_candidato = funcao_objetivo(candidato)
            delta = valor_candidato - valor_atual

            if delta > 0:
                # Melhor movimento: sempre aceita
                estado_atual, valor_atual = candidato, valor_candidato
            else:
                # Movimento pior: aceita com probabilidade exp(ΔE / T)
                probabilidade = math.exp(delta / temperatura)
                if random.random() < probabilidade:
                    estado_atual, valor_atual = candidato, valor_candidato

        print(f"🌡️ T = {temperatura:.4f} | Melhor x = {estado_atual:.4f}, f(x) = {valor_atual:.4f}")
        temperatura *= fator_resfriamento  # Resfriamento

    print(f"\n🏁 Melhor solução encontrada: x = {estado_atual:.4f}, f(x) = {valor_atual:.4f}")
```



*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 4.

---



### 5.4. Algoritmo Genético/Disruptivo Alternativo: Estratégias de Evolução (ES)

Dentro do campo da computação evolucionária, os Algoritmos Genéticos (GAs) são talvez os mais conhecidos, mas as Estratégias de Evolução (Evolution Strategies - ES), também mencionadas por Russell e Norvig (2013) no contexto de otimização, representam uma linha de desenvolvimento paralela e distinta, particularmente adequada para problemas de otimização em espaços de parâmetros contínuos. Enquanto os GAs clássicos frequentemente operam sobre representações binárias ou discretas (cromossomos) e dão grande ênfase ao operador de cruzamento (recombinação) para gerar novos indivíduos, as ES tipicamente trabalham diretamente com vetores de números reais que representam as soluções candidatas.

A principal força motriz da evolução nas ES é, muitas vezes, a mutação, e não o cruzamento (embora a recombinação também possa ser usada). A mutação em ES é geralmente implementada adicionando um vetor de ruído gaussiano (normalmente distribuído) ao vetor de parâmetros do indivíduo pai para criar um descendente. Um aspecto sofisticado de muitas ES modernas é a capacidade de adaptar os parâmetros da própria mutação (como as variâncias ou covariâncias da distribuição gaussiana) ao longo do processo evolutivo. Isso permite que o algoritmo ajuste a "força" e a "direção" da mutação dinamicamente, explorando mais amplamente no início e focando em regiões promissoras mais tarde.

Os mecanismos de seleção nas ES também podem diferir dos GAs. Duas notações comuns são (μ, λ)-ES e (μ + λ)-ES. Na (μ, λ)-ES, μ pais geram λ descendentes (λ ≥ μ), e os μ melhores *descendentes* formam a população da próxima geração, descartando completamente os pais. Isso permite que a ES escape de ótimos locais mais facilmente. Na (μ + λ)-ES, os μ melhores indivíduos são selecionados a partir da união dos μ pais *e* dos λ descendentes, garantindo que a melhor solução encontrada até o momento nunca seja perdida (elitismo). A escolha entre essas estratégias depende das características do problema.

Devido à sua afinidade com espaços contínuos e à adaptação de parâmetros de mutação, as Estratégias de Evolução tornaram-se uma ferramenta poderosa para a otimização de parâmetros em aprendizado de máquina (por exemplo, ajuste de hiperparâmetros ou treinamento direto de redes neurais), robótica, controle e outros domínios onde as soluções são naturalmente representadas por vetores de números reais. Elas oferecem uma alternativa robusta aos GAs quando a representação binária ou o cruzamento tradicional não são os mais adequados.

```python


import random

# Função objetivo: queremos minimizar f(x) = x^2
def funcao_objetivo(x):
    return x ** 2

# Estratégia de mutação: x' = x + N(0, sigma)
def mutacao(x, sigma):
    return x + random.gauss(0, sigma)

def evolution_strategy(mu=10, lamb=40, geracoes=100, sigma_inicial=1.0):
    # Geração inicial: números reais aleatórios
    populacao = [random.uniform(-5, 5) for _ in range(mu)]
    sigma = sigma_inicial

    for geracao in range(geracoes):
        descendentes = []

        # Cada pai gera λ/mu descendentes
        for _ in range(lamb):
            pai = random.choice(populacao)
            filho = mutacao(pai, sigma)
            descendentes.append(filho)

        # Combinar pais e descendentes
        combinados = populacao + descendentes

        # Selecionar os μ melhores
        populacao = sorted(combinados, key=funcao_objetivo)[:mu]

        # Opcional: adaptar sigma (ex: diminuir ao longo do tempo)
        sigma *= 0.99

        # Diagnóstico
        melhor = populacao[0]
        print(f"🧬 Geração {geracao+1}: Melhor x = {melhor:.4f}, f(x) = {funcao_objetivo(melhor):.4f}, σ = {sigma:.4f}")

    print(f"\n🏁 Solução final: x = {melhor:.4f}, f(x) = {funcao_objetivo(melhor):.4f}")


```



*Referência:* RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013. Capítulo 4 (mencionado brevemente no contexto de otimização estocástica).

---




## 4. Conclusão: Principais Aprendizados, Vantagens e Limitações

A resolução de problemas por busca é um dos pilares da Inteligência Artificial, fornecendo uma estrutura formal para abordar uma ampla gama de tarefas, desde jogos simples até problemas complexos do mundo real. O conceito central envolve a exploração de um espaço de estados para encontrar uma sequência de ações que leve a um estado objetivo.

**Principais Aprendizados:**

*   **Diversidade de Estratégias:** Aprendemos que existe uma vasta gama de estratégias de busca, cada uma com suas próprias características. As buscas cegas, como a Busca em Largura (BFS), são sistemáticas e podem garantir completude e otimalidade (em certos casos), mas frequentemente sofrem com alta complexidade de tempo e espaço. Por outro lado, as buscas informadas, como A*, utilizam heurísticas para guiar a exploração de forma mais eficiente, reduzindo drasticamente o esforço computacional quando a heurística é bem projetada. A A* se destaca por sua capacidade de encontrar o caminho de menor custo de forma completa e ótima, desde que sua heurística seja admissível.
*   **Importância das Heurísticas:** A qualidade da função heurística é crucial para o desempenho das buscas informadas. Uma boa heurística pode transformar um problema intratável em um solucionável, enquanto uma heurística ruim pode levar a um desempenho pior que o da busca cega.
*   **Busca em Ambientes Complexos:** Para problemas onde o espaço de estados é muito grande ou as soluções ótimas não são estritamente necessárias, algoritmos de busca local como o Hill Climbing oferecem uma alternativa eficiente em termos de memória. Embora possam ficar presos em máximos locais, técnicas como reinício aleatório podem mitigar esse problema. Eles são úteis para otimização contínua.
*   **Abordagens Evolutivas:** Algoritmos Genéticos representam uma classe de busca estocástica inspirada na evolução natural. Eles são robustos para lidar com espaços de busca complexos, multimodais e ruidosos. Através da manutenção de uma população de soluções e da aplicação de operadores genéticos (seleção, cruzamento, mutação), os AGs podem explorar globalmente o espaço de busca e encontrar soluções de alta qualidade, embora não garantam a otimalidade em tempo finito.
*   **Trade-offs:** A escolha do algoritmo de busca ideal envolve uma análise cuidadosa dos trade-offs entre completude, otimalidade, complexidade de tempo e complexidade de espaço, além da natureza do problema e da disponibilidade de informações heurísticas.

**Vantagens Gerais da Resolução de Problemas por Busca:**

*   **Generalidade:** A formulação de problemas como busca em um espaço de estados é uma abordagem muito geral, aplicável a diversos domínios.
*   **Fundamentação Teórica:** Muitos algoritmos de busca possuem uma base teórica sólida que permite analisar seu comportamento e garantias.
*   **Automatização do Raciocínio:** Permitem que agentes encontrem soluções para problemas sem intervenção humana direta, simulando formas de raciocínio.

**Limitações Gerais da Resolução de Problemas por Busca:**

*   **Explosão Combinatória:** Para muitos problemas, o tamanho do espaço de estados cresce exponencialmente com o tamanho do problema, tornando a busca exaustiva inviável (a "maldição da dimensionalidade").
*   **Representação do Problema:** A eficácia da busca depende criticamente de como o problema é formulado (definição de estados, ações, custos).
*   **Necessidade de Heurísticas (para eficiência):** Para problemas complexos, buscas cegas são frequentemente ineficientes, e o desenvolvimento de boas heurísticas pode ser um desafio em si.
*   **Máximos Locais e Platôs:** Algoritmos de busca local e alguns outros podem ficar presos em soluções subótimas devido à topografia do espaço de busca.

Em suma, as técnicas de resolução de problemas por busca são ferramentas essenciais no arsenal da Inteligência Artificial. A compreensão de suas diversas formas, vantagens e limitações permite aos desenvolvedores escolher e adaptar a abordagem mais adequada para construir sistemas inteligentes capazes de resolver problemas de forma eficaz e eficiente.

## 5. Referências Bibliográficas

LUGER, G. F. *Artificial Intelligence: Structures and Strategies for Complex Problem Solving*. 6. ed. Boston, MA: Pearson, 2009.

MARSLAND, S. *Machine Learning: An Algorithmic Perspective*. 2. ed. Boca Raton, FL: CRC Press, 2014.

RUSSELL, S. J.; NORVIG, P. *Artificial Intelligence: A Modern Approach*. 3. ed. Upper Saddle River, NJ: Prentice Hall, 2010.

SUTTON, R. S.; BARTO, A. G. *Reinforcement Learning: An Introduction*. 2. ed. Cambridge, MA: MIT Press, 2018.

DATACAMP. *Implementing the Hill Climbing Algorithm for AI in Python*. [S.l.]: DataCamp, [s.d.]. Disponível em: https://www.datacamp.com/tutorial/hill-climbing-algorithm-for-ai-in-python. Acesso em: 16 maio 2025.

**Materiais de Aula (Slides da Disciplina):**

FGA0221 – IA - 06. Material de aula da disciplina de Inteligência Artificial. [S.l.: s.n., s.d.].

FGA0221 – IA - 07. Material de aula da disciplina de Inteligência Artificial. [S.l.: s.n., s.d.].

FGA0221 – IA - 08. Material de aula da disciplina de Inteligência Artificial. [S.l.: s.n., s.d.].

FGA0221 – IA - 09. Material de aula da disciplina de Inteligência Artificial. [S.l.: s.n., s.d.].

*   Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3rd ed.). Prentice Hall.
*   Material da disciplina FGA0221 – IA - Slides 06.
*   Material da disciplina FGA0221 – IA - Slides 07.
*   Material da disciplina FGA0221 – IA - Slides 08.
*   Material da disciplina FGA0221 – IA - Slides 09.
*   Marsland, S. (2014). *Machine Learning: An Algorithmic Perspective* (2nd ed.). Chapman and Hall/CRC.
*   Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
*   Luger, G. F. (2009). *Artificial Intelligence: Structures and Strategies for Complex Problem Solving* (6th ed.). Pearson.

