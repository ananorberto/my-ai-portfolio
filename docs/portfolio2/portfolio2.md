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

## 3. Aplicações com Algoritmos

Aqui apresentamos exemplos de algoritmos de busca, seus problemas de aplicação, descrição e análise.

### 3.1 Algoritmo de Busca Cega: Busca em Largura (Breadth-First Search - BFS)

#### Descrição
A Busca em Largura é uma estratégia de busca cega que explora o espaço de estados expandindo todos os nós de um nível antes de passar para o próximo nível. Ela usa uma fila FIFO para gerenciar os nós a serem visitados. Podemos pensar nela como uma busca *best-first* onde a função de avaliação é a profundidade do nó.

#### Problema Aplicado
Um problema clássico onde a BFS pode ser aplicada é o problema do aspirador de pó.
*   *Estados:* A localização do aspirador e se há sujeira em cada uma das células. Para duas células, temos 8 estados possíveis (localização do agente (2) x sujeira célula 1 (2) x sujeira célula 2 (2)).
*   *Estado Inicial:* Qualquer estado é possível como inicial.
*   *Ações:* Mover para a esquerda, mover para a direita, aspirar.
*   *Modelo de Transição:* Descreve como as ações mudam o estado (ex: aspirar remove a sujeira na célula atual).
*   *Objetivo:* Ter todas as células limpas.
*   *Custo da Ação:* Cada ação custa 1 unidade.

Outro exemplo comum é encontrar o caminho mais curto entre dois nós em um grafo não ponderado, como o exemplo de código abaixo demonstra para um grafo genérico.

#### Algoritmo Comentado
O algoritmo inicia com o estado inicial na fila FIFO. Em cada passo, retira o primeiro nó da fila, verifica se é o objetivo. Se não for, gera seus sucessores (aplicando as ações possíveis), e adiciona esses sucessores ao final da fila.

```python
# Importa a coleção deque para implementar a fila de forma eficiente
from collections import deque

# Grafo de exemplo representado como um dicionário de adjacências
# As chaves são os nós e os valores são listas de seus vizinhos.
graph_exemplo_bfs = {
  'A' : ['B','C'],
  'B' : ['D','E'],
  'C' : ['F','G'],
  'D' : [],
  'E' : ['F'], # Adicionando uma conexão para tornar o grafo um pouco mais interessante
  'F' : [],
  'G' : []
}

# Função para a Busca em Largura (BFS)
def bfs(graph, start_node):
  # Conjunto para armazenar os nós já visitados e evitar ciclos e redundâncias
  visited = set()
  # Fila (queue) para gerenciar os nós a serem explorados, usando deque para eficiência (operações popleft e append)
  queue = deque()

  # Adiciona o nó inicial à fila e marca como visitado
  queue.append(start_node)
  visited.add(start_node)

  print(f"Iniciando BFS a partir do nó: {start_node}")
  print("Ordem de visitação dos nós:")

  # Loop principal: continua enquanto houver nós na fila para explorar
  while queue:
    # Remove o nó da frente da fila (FIFO - First-In, First-Out)
    current_node = queue.popleft()
    print(current_node, end=" ") # Processa/imprime o nó atual

    # Explora os vizinhos do nó atual
    for neighbour in graph[current_node]:
      # Se o vizinho ainda não foi visitado
      if neighbour not in visited:
        # Marca o vizinho como visitado
        visited.add(neighbour)
        # Adiciona o vizinho ao final da fila para exploração futura
        queue.append(neighbour)
  print("\nBFS concluída.")

# Código de Exemplo (Driver Code)
print("--- Exemplo de Busca em Largura (BFS) ---")
bfs(graph_exemplo_bfs, 'A') # Chama a função BFS começando pelo nó 'A'
```

#### Análise
A BFS é completa, ou seja, garante encontrar uma solução se houver uma. Para problemas onde todas as ações têm o mesmo custo (como no exemplo do aspirador onde cada ação custa 1, ou no exemplo de grafo acima onde cada aresta tem custo implícito de 1), a BFS é ótima, encontrando a solução com o menor número de passos/custo.

A principal desvantagem da BFS é o seu alto uso de memória. Em espaços de estados amplos, o número de nós a serem armazenados na fila pode crescer exponencialmente com a profundidade da solução (complexidade de espaço de O(b^d), onde 'b' é o fator de ramificação e 'd' é a profundidade da solução mais rasa). A complexidade de tempo também pode ser alta pela mesma razão (O(b^d)), pois no pior caso todos os nós até a profundidade 'd' são explorados. No entanto, sua completude e otimalidade (para custos uniformes) a tornam útil em certos cenários, como encontrar o caminho mais curto em termos de número de arestas em grafos não ponderados ou verificar a conectividade em um grafo.

### 3.2 Algoritmo de Busca Informada: A* (A-Estrela)

#### Descrição
Embora a busca A* não seja detalhada explicitamente nos slides, o conceito de busca informada e a busca *best-first* que utiliza uma fila de prioridade guiada por uma função de avaliação `f(n)` são apresentados. A busca informada usa uma função heurística `h(n)` que estima o custo restante para o objetivo. A busca *best-first* "gananciosa" (Greedy Best-First Search) usa `f(n) = h(n)`. A busca de custo uniforme (Uniform Cost Search) usa `f(n)` igual ao custo do caminho da raiz até o nó atual, `g(n)`. A busca A* combina esses conceitos, usando `f(n) = g(n) + h(n)`, onde `g(n)` é o custo do caminho do estado inicial até `n` e `h(n)` é a heurística que estima o custo de `n` até o objetivo. Isso a torna uma forma de busca *best-first* guiada pelo custo total estimado. Ela utiliza uma fila de prioridade para selecionar o próximo nó a ser expandido com base no menor valor de `f(n)`.

#### Problema Aplicado
Problemas de localização de rotas são exemplos ideais para busca informada, como encontrar o caminho mais curto entre duas cidades em um mapa. O exemplo de código abaixo ilustra a aplicação do A* para encontrar o caminho de menor custo em um grafo onde cada aresta tem um custo associado e cada nó tem um valor heurístico (estimativa de custo até o objetivo).

*   *Estados:* Nós no grafo (representando, por exemplo, cidades ou pontos em um mapa).
*   *Ações:* Mover de um nó para um adjacente através de uma aresta.
*   *Custo da Ação (`g(n)`):* O custo real para alcançar o nó `n` a partir do nó inicial.
*   *Objetivo:* Chegar ao nó de destino com o menor custo total.
*   *Heurística (`h(n)`):* Uma estimativa do custo do nó `n` até o nó objetivo. Para A* ser ótimo, a heurística deve ser admissível (nunca superestimar o custo real) e, idealmente, consistente.

#### Algoritmo Comentado
O algoritmo A* expande o nó na fila de prioridade com o menor valor de `f(n) = g(n) + h(n)`. Mantém registro do custo do caminho até cada nó (`g(n)`) e utiliza a heurística (`h(n)`) para estimar o custo restante.

```python
# Importa a biblioteca heapq para implementar a fila de prioridade de forma eficiente
import heapq

# Grafo de exemplo: dicionário onde as chaves são os nós e os valores são listas de tuplas.
# Cada tupla contém (vizinho, custo_real_para_vizinho).
graph_exemplo_a_star = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heurísticas (estimativa de custo do nó atual até o objetivo 'D')
# h(n) deve ser admissível (nunca superestimar o custo real)
heuristics_a_star = {
    'A': 3,  # Estimativa de A para D
    'B': 2,  # Estimativa de B para D
    'C': 1,  # Estimativa de C para D
    'D': 0   # Estimativa de D para D (objetivo)
}

# Função para a Busca A*
def a_star_search(graph, start_node, goal_node, heuristics):
    # Fila de prioridade para armazenar tuplas (f_score, g_score, node, path)
    # f_score = g_score + h_score
    # g_score é o custo real do início até o nó atual
    # h_score é o valor heurístico do nó atual até o objetivo
    priority_queue = []
    # Adiciona o nó inicial: (f_score, g_score, node, [path_to_node])
    # g_score inicial é 0, f_score inicial é g_score + heurística
    heapq.heappush(priority_queue, (0 + heuristics[start_node], 0, start_node, [start_node]))

    # Dicionário para armazenar o menor custo g_score encontrado até agora para cada nó
    # Isso ajuda a evitar caminhos subótimos e ciclos se um nó for alcançado com um custo menor
    g_scores = {node: float('inf') for node in graph}
    g_scores[start_node] = 0

    print(f"Iniciando A* de {start_node} para {goal_node}")

    while priority_queue:
        # Remove o nó com o menor f_score da fila de prioridade
        f_score, current_g_score, current_node, path = heapq.heappop(priority_queue)

        print(f"  Expandindo: {current_node} com f_score={f_score:.2f} (g={current_g_score:.2f}, h={heuristics[current_node]:.2f}), Caminho: {' -> '.join(path)}")

        # Se o nó atual é o objetivo, retorna o caminho e o custo
        if current_node == goal_node:
            print(f"Objetivo {goal_node} alcançado!")
            return path, current_g_score

        # Explora os vizinhos do nó atual
        for neighbour, cost_to_neighbour in graph[current_node]:
            # Calcula o g_score para o vizinho através do nó atual
            tentative_g_score = current_g_score + cost_to_neighbour

            # Se este caminho para o vizinho é melhor (menor g_score) do que qualquer caminho anterior
            if tentative_g_score < g_scores[neighbour]:
                # Atualiza o g_score do vizinho
                g_scores[neighbour] = tentative_g_score
                # Calcula o h_score (heurística) para o vizinho
                h_score_neighbour = heuristics[neighbour]
                # Calcula o f_score total para o vizinho
                f_score_neighbour = tentative_g_score + h_score_neighbour
                # Adiciona o vizinho à fila de prioridade com seu novo f_score e caminho atualizado
                new_path = path + [neighbour]
                heapq.heappush(priority_queue, (f_score_neighbour, tentative_g_score, neighbour, new_path))
                print(f"    Adicionando/Atualizando vizinho {neighbour}: f={f_score_neighbour:.2f} (g={tentative_g_score:.2f}, h={h_score_neighbour:.2f}), Caminho: {' -> '.join(new_path)}")

    # Se a fila de prioridade esvaziar e o objetivo não for alcançado, não há caminho
    print(f"Objetivo {goal_node} não alcançável a partir de {start_node}")
    return None, float('inf')

# Código de Exemplo (Driver Code)
print("\n--- Exemplo de Busca A* ---")
start_a_star = 'A'
goal_a_star = 'D'
path_a_star, cost_a_star = a_star_search(graph_exemplo_a_star, start_a_star, goal_a_star, heuristics_a_star)

if path_a_star:
    print(f"\nCaminho mais curto de {start_a_star} para {goal_a_star}: {' -> '.join(path_a_star)}")
    print(f"Custo total: {cost_a_star}")
else:
    print(f"Não foi encontrado caminho de {start_a_star} para {goal_a_star}.")

```

#### Análise
Se a heurística `h(n)` for admissível (nunca superestima o custo real para o objetivo) e consistente (ou monotônica, `h(n) <= custo(n, n') + h(n')` para todo vizinho `n'` de `n`), a busca A* é completa e ótima, encontrando a solução de menor custo. O uso da heurística permite que o algoritmo explore estados com maior probabilidade de levar rapidamente ao objetivo, sendo geralmente muito mais eficiente que a busca cega em problemas grandes.

A eficiência da A* depende crucialmente da qualidade da heurística. Uma heurística bem informada (mais próxima do custo real, sem superestimá-lo) reduz significativamente o espaço de busca explorado. Se `h(n) = 0` para todos os nós, A* se comporta como a Busca de Custo Uniforme. Se `h(n)` for muito alta e não admissível, A* pode não encontrar o caminho ótimo. No pior caso, se a heurística for ruim, a complexidade de tempo e espaço da A* pode ser exponencial, similar à busca cega, embora na prática, com boas heurísticas, o desempenho seja muito melhor. A necessidade de manter uma fila de prioridade e um registro dos custos `g(n)` pode consumir memória considerável para grafos grandes.

### 3.3 Algoritmo de Busca em Ambientes Complexos: Subida de Encosta (Hill Climbing)

#### Descrição
A Subida de Encosta (Hill Climbing) é um algoritmo de busca local iterativo que começa com uma solução arbitrária para um problema e tenta encontrar uma solução melhor fazendo uma mudança incremental na solução atual. Se a mudança produzir uma solução melhor, outra mudança incremental é feita para a nova solução, e assim por diante, até que nenhuma melhoria adicional possa ser encontrada. Ele é chamado de "subida de encosta" porque se assemelha a uma pessoa subindo uma colina: o objetivo é alcançar o pico (a melhor solução), e a pessoa só pode ver os arredores imediatos e se mover para um ponto mais alto.

Existem algumas variantes principais:
*   **Subida de Encosta Simples (Simple Hill Climbing):** Examina os vizinhos um por um e seleciona o primeiro vizinho que é melhor que o estado atual.
*   **Subida de Encosta de Maior Aclive (Steepest-Ascent Hill Climbing):** Examina todos os vizinhos do estado atual e seleciona aquele que oferece a maior melhoria.
*   **Subida de Encosta Estocástica (Stochastic Hill Climbing):** Escolhe um vizinho aleatoriamente entre os que são melhores. A probabilidade de escolha pode ser ponderada pela magnitude da melhoria.

Este algoritmo não mantém um histórico de busca, olhando apenas para o estado atual e seus vizinhos imediatos, o que o torna eficiente em termos de memória.

#### Problema Aplicado
O problema das N-Rainhas é um exemplo clássico onde a busca local, como o Hill Climbing, pode ser aplicada. O objetivo é colocar N rainhas em um tabuleiro de xadrez N×N de forma que nenhuma rainha ameace outra. Ou seja, não deve haver duas rainhas na mesma linha, coluna ou diagonal.

*   **Estado:** Uma configuração de N rainhas no tabuleiro, geralmente com uma rainha por coluna. O estado pode ser representado por um array de N inteiros, onde `array[i]` é a linha da rainha na coluna `i`.
*   **Função de Avaliação (Heurística):** O número de pares de rainhas que se atacam mutuamente. O objetivo é minimizar esse valor para 0.
*   **Vizinhos:** Um estado vizinho é gerado movendo uma única rainha para uma nova linha dentro de sua coluna atual.

#### Algoritmo Comentado (N-Rainhas com Hill Climbing de Maior Aclive)
O algoritmo começa com uma configuração aleatória de rainhas. Em cada iteração, ele avalia todos os possíveis movimentos de uma única rainha para uma nova linha em sua coluna. Ele escolhe o movimento que resulta na menor quantidade de ataques. Se nenhum movimento puder reduzir o número de ataques, o algoritmo pode ter atingido um máximo local (ou um platô) e para.

```python
import random

def calcular_ataques(configuracao):
    """Calcula o número de pares de rainhas se atacando."""
    n = len(configuracao)
    ataques = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Verifica ataques na mesma linha
            if configuracao[i] == configuracao[j]:
                ataques += 1
            # Verifica ataques na diagonal
            if abs(configuracao[i] - configuracao[j]) == abs(i - j):
                ataques += 1
    return ataques

def gerar_vizinhos(configuracao):
    """Gera todos os vizinhos movendo uma rainha por vez em sua coluna."""
    n = len(configuracao)
    vizinhos = []
    for col in range(n):
        config_original_linha = configuracao[col]
        for linha in range(n):
            if configuracao[col] != linha: # Se for uma nova linha para a rainha na coluna `col`
                nova_config = list(configuracao)
                nova_config[col] = linha
                vizinhos.append(tuple(nova_config))
    return vizinhos

def hill_climbing_n_rainhas(n, max_iteracoes_sem_melhora=100):
    """Resolve o problema das N-Rainhas usando Hill Climbing (subida de encosta de maior aclive)."""
    # Gera uma configuração inicial aleatória (uma rainha por coluna)
    configuracao_atual = [random.randint(0, n - 1) for _ in range(n)]
    ataques_atuais = calcular_ataques(configuracao_atual)
    print(f"Configuração Inicial: {configuracao_atual}, Ataques: {ataques_atuais}")

    iteracoes_sem_melhora = 0
    iteracao_total = 0

    while ataques_atuais > 0 and iteracoes_sem_melhora < max_iteracoes_sem_melhora:
        iteracao_total += 1
        melhor_vizinho = None
        melhores_ataques_vizinho = ataques_atuais

        # Avalia todos os vizinhos (movendo uma rainha por vez)
        for vizinho in gerar_vizinhos(configuracao_atual):
            ataques_vizinho = calcular_ataques(vizinho)
            if ataques_vizinho < melhores_ataques_vizinho:
                melhores_ataques_vizinho = ataques_vizinho
                melhor_vizinho = vizinho
            # Critério de desempate: se o número de ataques for igual, escolhe aleatoriamente para evitar platôs simples
            elif ataques_vizinho == melhores_ataques_vizinho and melhor_vizinho is not None and random.random() < 0.3:
                 melhor_vizinho = vizinho

        if melhor_vizinho is not None and melhores_ataques_vizinho < ataques_atuais:
            configuracao_atual = list(melhor_vizinho)
            ataques_atuais = melhores_ataques_vizinho
            iteracoes_sem_melhora = 0 # Reseta o contador pois houve melhora
            print(f"Iteração {iteracao_total}: Nova Config: {configuracao_atual}, Ataques: {ataques_atuais}")
        else:
            # Não houve melhora ou o melhor vizinho não é estritamente melhor
            iteracoes_sem_melhora += 1
            print(f"Iteração {iteracao_total}: Sem melhora. Ataques: {ataques_atuais}. Iterações sem melhora: {iteracoes_sem_melhora}")
            # Se preso, pode tentar um reinício aleatório (não implementado aqui para simplicidade)
            # ou simplesmente parar se atingir o limite de iterações sem melhora.

    if ataques_atuais == 0:
        print(f"\nSolução encontrada para {n}-Rainhas após {iteracao_total} iterações!")
        print(f"Configuração Final: {configuracao_atual}, Ataques: {ataques_atuais}")
    else:
        print(f"\nNão foi encontrada uma solução ótima após {iteracao_total} iterações (máximo local ou platô). Parou com {ataques_atuais} ataques.")
        print(f"Configuração Final: {configuracao_atual}")
    return configuracao_atual, ataques_atuais

# Código de Exemplo (Driver Code)
print("\n--- Exemplo de Hill Climbing para N-Rainhas ---")
numero_de_rainhas = 8 # Tente com 4, 8, etc.
config_final, ataques_finais = hill_climbing_n_rainhas(numero_de_rainhas)

# Para visualizar o tabuleiro (opcional)
def imprimir_tabuleiro(configuracao):
    n = len(configuracao)
    for i in range(n):
        linha_str = ""
        for j in range(n):
            if configuracao[j] == i:
                linha_str += " Q "
            else:
                linha_str += " . "
        print(linha_str)

if ataques_finais == 0:
    print("\nTabuleiro da Solução:")
    imprimir_tabuleiro(config_final)

```

#### Análise
**Vantagens:**
*   **Simplicidade:** O algoritmo é relativamente fácil de entender e implementar.
*   **Eficiência de Memória:** Requer pouca memória, pois armazena apenas o estado atual e, possivelmente, um vizinho.
*   **Rapidez (em alguns casos):** Pode encontrar soluções boas ou ótimas rapidamente para certos problemas se a paisagem de busca for favorável.

**Limitações:**
*   **Máximos Locais:** O algoritmo pode ficar preso em um máximo local, que é um pico na paisagem de busca onde todos os vizinhos são piores, mas que não é a solução global ótima. No problema das N-Rainhas, isso significa uma configuração onde qualquer movimento de uma única rainha aumenta o número de ataques, mas a configuração ainda tem ataques.
*   **Platôs:** São regiões planas no espaço de busca onde todos os vizinhos têm o mesmo valor de avaliação que o estado atual. O algoritmo pode vagar indefinidamente ou parar prematuramente.
*   **Cumeeiras (Ridges):** São sequências de máximos locais de difícil navegação, onde o algoritmo pode ter que se mover para uma solução pior para, eventualmente, encontrar uma melhor.
*   **Incompletude:** Não garante encontrar a solução ótima global e pode nem mesmo encontrar uma solução se ficar preso.

**Estratégias para Superar Limitações:**
*   **Reinício Aleatório (Random-Restart Hill Climbing):** Se o algoritmo ficar preso, ele é reiniciado a partir de um novo estado inicial aleatório. Isso é repetido várias vezes, e a melhor solução encontrada é mantida.
*   **Subida de Encosta Estocástica:** Introduz aleatoriedade na escolha do próximo estado, permitindo movimentos que não são os melhores localmente.
*   **Simulated Annealing (Recozimento Simulado):** Permite movimentos para estados piores com uma certa probabilidade, que diminui ao longo do tempo. Isso ajuda a escapar de máximos locais.
*   **Busca Tabu:** Mantém uma lista de movimentos recentes (tabu) para evitar ciclos e revisitar soluções já exploradas.

Para o problema das N-Rainhas, o Hill Climbing simples pode frequentemente ficar preso. O reinício aleatório é uma técnica comum para melhorar suas chances de encontrar uma solução ótima.

### 3.4 Algoritmo Genético (ou Disruptivo)

#### Descrição
Algoritmos Genéticos (AGs) são algoritmos de busca e otimização inspirados nos princípios da evolução natural e genética. Eles operam sobre uma população de soluções candidatas (indivíduos ou cromossomos), aplicando operadores genéticos como seleção, cruzamento (crossover) e mutação para evoluir a população em direção a soluções melhores ao longo de gerações. Cada indivíduo na população representa uma possível solução para o problema, e sua "qualidade" é avaliada por uma função de aptidão (fitness function).

O processo geral de um AG é:
1.  **Inicialização:** Criação de uma população inicial de indivíduos (geralmente aleatória).
2.  **Avaliação:** Cálculo da aptidão de cada indivíduo na população.
3.  **Seleção:** Seleção dos indivíduos mais aptos para serem pais da próxima geração. Indivíduos com maior aptidão têm maior probabilidade de serem selecionados.
4.  **Cruzamento (Crossover):** Pares de pais selecionados trocam partes de suas representações (cromossomos) para criar descendentes (filhos), combinando características dos pais.
5.  **Mutação:** Pequenas alterações aleatórias são introduzidas nos cromossomos dos descendentes para manter a diversidade genética e explorar novas áreas do espaço de busca.
6.  **Substituição:** A nova geração de descendentes substitui a população anterior (ou parte dela).
7.  **Repetição:** Os passos de avaliação, seleção, cruzamento e mutação são repetidos por um número de gerações ou até que um critério de parada seja atingido (ex: encontrar uma solução satisfatória ou o tempo limite esgotar).

AGs são particularmente úteis para problemas de otimização complexos, onde o espaço de busca é grande, não linear ou multimodal, e onde métodos tradicionais podem falhar ou ser ineficientes.

#### Problema Aplicado
O problema "OneMax" (ou "Maximizar Uns") é um problema de brinquedo clássico usado para testar e demonstrar algoritmos genéticos. O objetivo é encontrar uma string binária (uma sequência de 0s e 1s) de um determinado comprimento que contenha o maior número possível de 1s. A solução ótima é uma string composta inteiramente por 1s.

*   **Indivíduo (Cromossomo):** Uma string binária de comprimento `N` (ex: `[1, 0, 1, 1, 0, ..., 1]`).
*   **Função de Aptidão (Fitness Function):** O número de 1s na string binária. O objetivo é maximizar essa função (ou minimizar a contagem de 0s, como no exemplo de código que visa minimizar a soma negativa).
*   **Seleção:** Pode ser feita por torneio, roleta, etc.
*   **Cruzamento:** Crossover de um ponto, dois pontos ou uniforme.
*   **Mutação:** Inverter um bit aleatoriamente (0 para 1, 1 para 0) com uma pequena probabilidade.

Embora simples, o OneMax ilustra bem os mecanismos básicos de um AG.

#### Algoritmo Comentado (OneMax com Algoritmo Genético)
O código abaixo implementa um algoritmo genético para resolver o problema OneMax.

```python
import random

# Função de aptidão (objetivo): maximizar o número de 1s.
# No código original fornecido, a função onemax(x) retorna -sum(x),
# o que significa que o AG tentará minimizar essa soma negativa,
# o que é equivalente a maximizar a soma (número de 1s).
def funcao_aptidao_onemax(individuo):
    """Calcula a aptidão de um indivíduo (string binária) contando o número de 1s."""
    return sum(individuo)

# Seleção por torneio: seleciona k indivíduos aleatoriamente e retorna o melhor deles.
def selecao_torneio(populacao, aptidoes, k=3):
    """Seleciona um pai da população usando seleção por torneio."""
    # Seleciona o primeiro candidato aleatoriamente
    indice_melhor_candidato = random.randrange(len(populacao))
    # Seleciona os outros k-1 candidatos aleatoriamente
    for _ in range(k - 1):
        indice_candidato_atual = random.randrange(len(populacao))
        # Se o candidato atual for melhor (maior aptidão), atualiza o melhor
        if aptidoes[indice_candidato_atual] > aptidoes[indice_melhor_candidato]:
            indice_melhor_candidato = indice_candidato_atual
    return populacao[indice_melhor_candidato]

# Cruzamento (Crossover) de um ponto.
def cruzamento_um_ponto(pai1, pai2, taxa_cruzamento):
    """Realiza o cruzamento entre dois pais para gerar dois filhos."""
    filho1, filho2 = list(pai1), list(pai2) # Cria cópias dos pais
    if random.random() < taxa_cruzamento:
        # Escolhe um ponto de cruzamento aleatório (não nas extremidades)
        if len(pai1) > 1:
            ponto_cruzamento = random.randint(1, len(pai1) - 1)
            # Realiza o cruzamento
            filho1 = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]
            filho2 = pai2[:ponto_cruzamento] + pai1[ponto_cruzamento:]
    return [filho1, filho2]

# Mutação bit-flip: inverte cada bit com uma pequena probabilidade.
def mutacao_bit_flip(individuo, taxa_mutacao):
    """Realiza a mutação em um indivíduo (inverte bits aleatoriamente)."""
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i] # Inverte o bit (0->1, 1->0)

# Algoritmo Genético principal
def algoritmo_genetico_onemax(func_aptidao, n_bits, n_geracoes, tam_populacao, taxa_cruzamento, taxa_mutacao):
    """Executa o algoritmo genético para o problema OneMax."""
    # Inicializa a população com indivíduos (strings binárias) aleatórios
    populacao = [[random.randint(0, 1) for _ in range(n_bits)] for _ in range(tam_populacao)]
    
    melhor_individuo_global = None
    melhor_aptidao_global = -1 # Começa com a pior aptidão possível para maximização

    print(f"Iniciando Algoritmo Genético para OneMax ({n_bits} bits)")

    # Loop através das gerações
    for geracao in range(n_geracoes):
        # Avalia a aptidão de cada indivíduo na população atual
        aptidoes = [func_aptidao(ind) for ind in populacao]

        # Encontra o melhor indivíduo desta geração e o melhor global até agora
        for i in range(tam_populacao):
            if aptidoes[i] > melhor_aptidao_global:
                melhor_aptidao_global = aptidoes[i]
                melhor_individuo_global = list(populacao[i]) # Armazena uma cópia
                print(f">Geração {geracao:3d}, Novo Melhor Global! Aptidão: {melhor_aptidao_global}, Indivíduo: {melhor_individuo_global}")
        
        # Se a solução ótima for encontrada (todos os bits são 1), para mais cedo
        if melhor_aptidao_global == n_bits:
            print(f"Solução ótima encontrada na geração {geracao}!")
            break

        # Seleciona os pais para a próxima geração
        # Aqui, para simplificar, vamos gerar uma nova população do mesmo tamanho
        pais_selecionados = [selecao_torneio(populacao, aptidoes) for _ in range(tam_populacao)]
        
        # Cria a próxima geração através de cruzamento e mutação
        proxima_geracao = []
        for i in range(0, tam_populacao, 2):
            # Pega os pais em pares
            # Garante que tenhamos pares, mesmo que a população seja ímpar (o último pode não ter par)
            if i + 1 < len(pais_selecionados):
                pai1, pai2 = pais_selecionados[i], pais_selecionados[i+1]
                # Realiza o cruzamento
                for filho in cruzamento_um_ponto(pai1, pai2, taxa_cruzamento):
                    # Realiza a mutação no filho
                    mutacao_bit_flip(filho, taxa_mutacao)
                    # Adiciona o filho à próxima geração
                    proxima_geracao.append(filho)
            else: # Caso de população ímpar, o último pai pode passar diretamente ou ser duplicado
                proxima_geracao.append(list(pais_selecionados[i]))
        
        # Garante que a próxima geração tenha o tamanho correto (pode ser um pouco menor/maior devido ao cruzamento)
        # Se menor, podemos preencher com alguns dos melhores da geração anterior ou aleatórios
        # Se maior, podemos truncar. Para este exemplo, vamos apenas substituir.
        if len(proxima_geracao) < tam_populacao:
             # Preenche com os melhores da geração anterior se necessário
            proxima_geracao.extend(sorted(populacao, key=func_aptidao, reverse=True)[:tam_populacao - len(proxima_geracao)])
        
        populacao = proxima_geracao[:tam_populacao] # Atualiza a população

        if (geracao + 1) % 10 == 0 or geracao == n_geracoes -1 : # Imprime progresso
            print(f"Geração {geracao+1:3d} concluída. Melhor aptidão atual na população: {max(aptidoes) if aptidoes else 'N/A'}. Melhor global: {melhor_aptidao_global}")

    print("\nAlgoritmo Genético concluído!")
    return melhor_individuo_global, melhor_aptidao_global

# Parâmetros do Algoritmo Genético
NUM_BITS = 20          # Comprimento da string binária (cromossomo)
NUM_GERACOES = 100     # Número de gerações para executar
TAMANHO_POPULACAO = 50 # Número de indivíduos na população
TAXA_CRUZAMENTO = 0.9  # Probabilidade de cruzamento entre pais
TAXA_MUTACAO = 1.0 / float(NUM_BITS) # Probabilidade de mutação de um bit (comum ser 1/comprimento_cromossomo)

# Executa o Algoritmo Genético
print("\n--- Exemplo de Algoritmo Genético para o Problema OneMax ---")
melhor_solucao, aptidao_da_melhor = algoritmo_genetico_onemax(
    funcao_aptidao_onemax,
    NUM_BITS,
    NUM_GERACOES,
    TAMANHO_POPULACAO,
    TAXA_CRUZAMENTO,
    TAXA_MUTACAO
)

print(f"\nMelhor solução encontrada: {melhor_solucao}")
print(f"Aptidão da melhor solução (número de 1s): {aptidao_da_melhor}")

```

#### Análise
**Vantagens dos Algoritmos Genéticos:**
*   **Robustez:** São eficazes em espaços de busca complexos, ruidosos, multimodais e não diferenciáveis, onde algoritmos tradicionais podem falhar.
*   **Paralelismo inerente:** A avaliação da aptidão dos indivíduos pode ser feita em paralelo.
*   **Exploração Global:** Têm uma boa capacidade de explorar diferentes regiões do espaço de busca, ajudando a evitar máximos locais prematuramente, especialmente com taxas de mutação adequadas.
*   **Ampla Aplicabilidade:** Podem ser aplicados a uma vasta gama de problemas de otimização e busca, desde que uma representação de cromossomo e uma função de aptidão possam ser definidas.
*   **Não requerem conhecimento do gradiente:** Diferentemente de métodos baseados em gradiente, não precisam de informações sobre a derivada da função objetivo.

**Limitações dos Algoritmos Genéticos:**
*   **Convergência Prematura:** Podem convergir para um máximo local se a diversidade genética for perdida muito rapidamente (ex: seleção muito forte ou taxa de mutação muito baixa).
*   **Ajuste de Parâmetros:** O desempenho de um AG pode ser sensível à escolha de seus parâmetros (tamanho da população, taxas de cruzamento e mutação, tipo de seleção, etc.), que muitas vezes precisam ser ajustados empiricamente.
*   **Custo Computacional:** Podem ser computacionalmente caros, especialmente para funções de aptidão complexas ou populações grandes e muitas gerações.
*   **Representação:** Definir uma boa representação do cromossomo para o problema pode ser desafiador.
*   **Garantia de Otimização:** Não há garantia de que encontrarão a solução ótima global em um tempo finito, embora frequentemente encontrem soluções muito boas.

Os Algoritmos Genéticos são uma ferramenta poderosa no campo da computação evolutiva e têm sido aplicados com sucesso em áreas como design de engenharia, planejamento, aprendizado de máquina (ex: otimização de hiperparâmetros de redes neurais), roteamento, bioinformática e muito mais.

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

