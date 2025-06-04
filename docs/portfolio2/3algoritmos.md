## 3. Análise de Algoritmos de Busca

### 3.1 Algoritmos de Busca Cega (Uninformed Search)

Quando falamos de algoritmos de busca cega (ou não informada), estamos nos referindo àqueles que exploram o espaço de estados sem ter nenhuma pista sobre quão próximos estamos do objetivo. É como tentar encontrar um caminho no escuro. Os principais tipos são:

*   **Busca em Largura (Breadth-First Search - BFS):** Expande sistematicamente os nós mais rasos e não expandidos primeiro. Garante encontrar a solução mais rasa (ótima em termos de número de passos se os custos forem uniformes), mas pode exigir muita memória.
*   **Busca de Custo Uniforme (Uniform-Cost Search - UCS):** Expande o nó não expandido com o menor custo de caminho acumulado (`g(n)`). É ótima e completa, desde que os custos dos passos sejam não negativos. É essencialmente uma generalização da BFS para custos de passo variáveis.
*   **Busca em Profundidade (Depth-First Search - DFS):** Expande sempre o nó mais profundo na fronteira da árvore de busca. Usa menos memória que a BFS (ordem linear em relação à profundidade máxima), mas não é completa (pode se perder em caminhos infinitos) nem ótima por si só.
*   **Busca com Aprofundamento Iterativo (Iterative Deepening Depth-First Search - IDDFS ou IDS):** Combina os benefícios da BFS (completude e otimalidade para custos uniformes) e da DFS (requisitos modestos de memória). Realiza buscas em profundidade com limites de profundidade crescentes (1, 2, 3, ...), até encontrar a solução. Embora pareça redundante por repetir expansões, é geralmente o método de busca cega preferido quando o espaço de busca é grande e a profundidade da solução é desconhecida.
*   **Busca Bidirecional (Bidirectional Search):** Executa duas buscas simultâneas, uma partindo do estado inicial e outra partindo do estado objetivo (se as ações forem reversíveis), parando quando as duas buscas se encontram no meio. Pode reduzir drasticamente a complexidade de tempo e espaço, explorando uma área muito menor do espaço de estados em comparação com buscas unidirecionais.

#### 3.1.1 Implementação da Busca Bidirecional

A Busca Bidirecional é uma técnica poderosa que executa duas buscas simultâneas - uma partindo do estado inicial e outra do estado objetivo - até que os dois caminhos se encontrem. Esta abordagem pode reduzir significativamente o espaço de busca explorado, especialmente em grafos grandes.

```python
from collections import deque

def busca_bidirecional(grafo, inicio, objetivo):
    """
    Implementação da Busca Bidirecional para encontrar o caminho mais curto
    entre os nós 'inicio' e 'objetivo' em um grafo.
    
    Args:
        grafo: Dicionário onde as chaves são nós e os valores são listas de vizinhos
        inicio: Nó inicial
        objetivo: Nó objetivo
    
    Returns:
        O caminho mais curto, ou None se não existir
    """
    # Verifica se o grafo é bidirecional (todos os caminhos são reversíveis)
    if not verificar_bidirecional(grafo):
        print("Aviso: O grafo não é bidirecional. A busca bidirecional pode não funcionar corretamente.")
    
    # Inicializa as filas para busca em ambas as direções
    fila_inicio = deque([(inicio, [inicio])])  # (nó atual, caminho até o nó)
    fila_objetivo = deque([(objetivo, [objetivo])])
    
    # Conjuntos para rastrear nós visitados em cada direção
    visitados_inicio = {inicio: [inicio]}  # nó: caminho
    visitados_objetivo = {objetivo: [objetivo]}
    
    # Contadores para análise de desempenho
    nos_expandidos = 0
    
    print(f"Iniciando Busca Bidirecional de {inicio} para {objetivo}")
    
    while fila_inicio and fila_objetivo:
        # Expande um nível da busca a partir do início
        nos_expandidos += expandir_nivel(grafo, fila_inicio, visitados_inicio, visitados_objetivo, "início")
        
        # Expande um nível da busca a partir do objetivo
        nos_expandidos += expandir_nivel(grafo, fila_objetivo, visitados_objetivo, visitados_inicio, "objetivo")
    
    print(f"Não foi possível encontrar um caminho até {objetivo}")
    print(f"Total de nós expandidos: {nos_expandidos}")
    return None

def expandir_nivel(grafo, fila, visitados_atual, visitados_outro, direcao):
    """
    Expande um nível da busca em uma direção.
    
    Args:
        grafo: O grafo do problema
        fila: A fila de busca atual
        visitados_atual: Dicionário de nós visitados na direção atual
        visitados_outro: Dicionário de nós visitados na outra direção
        direcao: String indicando a direção ("início" ou "objetivo")
    
    Returns:
        Número de nós expandidos
    """
    if not fila:
        return 0
    
    nos_expandidos = 0
    tamanho_nivel = len(fila)
    
    for _ in range(tamanho_nivel):
        no_atual, caminho_atual = fila.popleft()
        nos_expandidos += 1
        
        print(f"Expandindo nó {no_atual} na direção {direcao}")
        
        # Verifica se encontramos um caminho comum
        if no_atual in visitados_outro:
            caminho_outro = visitados_outro[no_atual]
            if direcao == "início":
                caminho_completo = caminho_atual + caminho_outro[::-1][1:]
            else:
                caminho_completo = caminho_outro + caminho_atual[::-1][1:]
            
            print(f"Caminho encontrado! Nó de encontro: {no_atual}")
            print(f"Caminho completo: {caminho_completo}")
            print(f"Total de nós expandidos: {nos_expandidos}")
            return caminho_completo
        
        # Expande os vizinhos
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados_atual:
                novo_caminho = caminho_atual + [vizinho]
                visitados_atual[vizinho] = novo_caminho
                fila.append((vizinho, novo_caminho))
                print(f"  Adicionando vizinho {vizinho} à fila {direcao}")
    
    return nos_expandidos

def verificar_bidirecional(grafo):
    """
    Verifica se o grafo é bidirecional (todos os caminhos são reversíveis).
    
    Args:
        grafo: O grafo a ser verificado
    
    Returns:
        True se o grafo for bidirecional, False caso contrário
    """
    for no, vizinhos in grafo.items():
        for vizinho in vizinhos:
            if no not in grafo.get(vizinho, []):
                return False
    return True

# Exemplo de uso
if __name__ == "__main__":
    # Grafo representando um mapa simples
    mapa = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Busca um caminho de A até F
    caminho = busca_bidirecional(mapa, 'A', 'F')
    
    if caminho:
        print(f"Caminho encontrado: {' -> '.join(caminho)}")
    else:
        print("Não existe caminho entre os pontos especificados.")
```

### 3.2 Algoritmos de Busca Informada (Heurística)

Os algoritmos de busca informada, ou busca heurística, utilizam conhecimento específico do problema, na forma de uma função heurística `h(n)`, para estimar a distância (ou custo) de um estado `n` até o objetivo. Essa informação guia a busca de forma mais eficiente, priorizando caminhos que parecem mais promissores. Russell e Norvig (2013) destacam as seguintes abordagens:

*   **Busca Best-First Genérica (Generic Best-First Search):** É um paradigma de busca que seleciona o próximo nó a ser expandido com base em uma função de avaliação `f(n)`. Diferentes algoritmos best-first surgem da escolha de diferentes funções `f`.
*   **Busca Best-First Gulosa (Greedy Best-First Search):** Uma instância da busca best-first que tenta expandir o nó que está estimado como o mais próximo do objetivo, usando a função heurística diretamente como função de avaliação: `f(n) = h(n)`. Embora possa ser rápida, não é ótima nem completa.
*   **Busca A* (A* Search):** Considerado o algoritmo de busca heurística mais conhecido, A* combina o custo do caminho percorrido desde o início (`g(n)`) com a estimativa heurística do custo restante até o objetivo (`h(n)`), utilizando a função de avaliação `f(n) = g(n) + h(n)`. A* é completo e ótimo, desde que a heurística `h(n)` seja admissível (nunca superestima o custo real) e, para eficiência ótima, consistente. É amplamente utilizado em problemas de planejamento de caminhos e outros.
*   **Buscas Heurísticas com Memória Limitada:** Como A* pode consumir muita memória, foram desenvolvidas variantes que operam com restrições de espaço:
    *   **Busca Recursiva Best-First (Recursive Best-First Search - RBFS):** Simula a operação de A* usando apenas espaço linear. Faz isso explorando um caminho e mantendo o valor `f` do melhor caminho alternativo a partir de seus ancestrais. Se o custo do caminho atual exceder esse valor limite, ele retrocede e explora o caminho alternativo. Pode sofrer de recomputação excessiva.
    *   **SMA* (Simplified Memory-Bounded A*):** Utiliza toda a memória disponível. Expande os melhores nós folha até que a memória esteja cheia. Nesse ponto, remove o nó folha com o maior valor `f` (o pior) para liberar espaço para um novo nó. É completo se houver memória suficiente para armazenar o caminho da solução mais rasa e ótimo se encontrar uma solução.
*   **Aprendizado de Heurísticas (Learning Heuristics):** Abordagens onde a função heurística não é dada a priori, mas aprendida a partir da experiência ou de exemplos do problema, como resolver subproblemas mais simples (bases de dados de padrões) ou através de aprendizado indutivo.

#### 3.2.1 Implementação da Greedy Best-First Search

A Greedy Best-First Search é um algoritmo de busca informada que utiliza apenas a função heurística para guiar a busca, sempre escolhendo expandir o nó que parece estar mais próximo do objetivo. Diferente do A*, ela não considera o custo do caminho já percorrido.

```python
import heapq

def busca_gulosa(grafo, inicio, objetivo, heuristica):
    """
    Implementação da Greedy Best-First Search para encontrar um caminho
    entre os nós 'inicio' e 'objetivo' em um grafo, usando uma função heurística.
    
    Args:
        grafo: Dicionário onde as chaves são nós e os valores são dicionários
               de vizinhos com seus respectivos custos {vizinho: custo}
        inicio: Nó inicial
        objetivo: Nó objetivo
        heuristica: Função que estima a distância de um nó até o objetivo
    
    Returns:
        O caminho encontrado, ou None se não existir
    """
    # Fila de prioridade para os nós a serem expandidos
    # Formato: (valor_heuristico, contador, nó, caminho)
    # contador é usado para desempate quando valores heurísticos são iguais
    fila_prioridade = [(heuristica(inicio, objetivo), 0, inicio, [inicio])]
    
    # Conjunto para rastrear nós visitados
    visitados = set([inicio])
    
    # Contador para desempate e para rastrear nós expandidos
    contador = 1
    nos_expandidos = 0
    
    print(f"Iniciando Busca Gulosa a partir de {inicio}, buscando {objetivo}")
    print(f"Valor heurístico inicial: h({inicio}) = {heuristica(inicio, objetivo)}")
    
    while fila_prioridade:
        # Retira o nó com menor valor heurístico
        _, _, no_atual, caminho = heapq.heappop(fila_prioridade)
        nos_expandidos += 1
        
        print(f"Expandindo nó: {no_atual}, Caminho até aqui: {caminho}")
        
        # Verifica se chegamos ao objetivo
        if no_atual == objetivo:
            print(f"Objetivo encontrado! Caminho: {caminho}")
            print(f"Total de nós expandidos: {nos_expandidos}")
            return caminho
        
        # Explora todos os vizinhos não visitados
        for vizinho in grafo.get(no_atual, {}).keys():
            if vizinho not in visitados:
                # Marca como visitado
                visitados.add(vizinho)
                
                # Calcula o valor heurístico do vizinho
                h_valor = heuristica(vizinho, objetivo)
                
                # Adiciona à fila de prioridade
                novo_caminho = caminho + [vizinho]
                heapq.heappush(fila_prioridade, (h_valor, contador, vizinho, novo_caminho))
                contador += 1
                
                print(f"  Adicionando vizinho {vizinho} à fila, h={h_valor}")
    
    # Se a fila esvaziar sem encontrar o objetivo, não há caminho
    print(f"Não foi possível encontrar um caminho até {objetivo}")
    print(f"Total de nós expandidos: {nos_expandidos}")
    return None

# Função heurística de exemplo: distância Manhattan em uma grade 2D
def distancia_manhattan(ponto1, ponto2):
    """
    Calcula a distância Manhattan entre dois pontos em uma grade 2D.
    Assume que os pontos são representados como strings 'x,y'.
    """
    x1, y1 = map(int, ponto1.split(','))
    x2, y2 = map(int, ponto2.split(','))
    return abs(x1 - x2) + abs(y1 - y2)

# Exemplo de uso
if __name__ == "__main__":
    # Grafo representando uma grade 2D com obstáculos
    # Formato: {nó: {vizinho1: custo1, vizinho2: custo2, ...}}
    grade = {
        '0,0': {'1,0': 1, '0,1': 1},
        '0,1': {'0,0': 1, '0,2': 1, '1,1': 1},
        '0,2': {'0,1': 1, '1,2': 1},
        '1,0': {'0,0': 1, '2,0': 1, '1,1': 1},
        '1,1': {'0,1': 1, '1,0': 1, '1,2': 1, '2,1': 1},
        '1,2': {'0,2': 1, '1,1': 1, '2,2': 1},
        '2,0': {'1,0': 1, '3,0': 1, '2,1': 1},
        '2,1': {'1,1': 1, '2,0': 1, '2,2': 1, '3,1': 1},
        '2,2': {'1,2': 1, '2,1': 1, '3,2': 1},
        '3,0': {'2,0': 1, '3,1': 1},
        '3,1': {'3,0': 1, '2,1': 1, '3,2': 1},
        '3,2': {'3,1': 1, '2,2': 1}
    }
    
    # Busca um caminho de (0,0) até (3,2)
    caminho = busca_gulosa(grade, '0,0', '3,2', distancia_manhattan)
    
    if caminho:
        print(f"Caminho encontrado: {' -> '.join(caminho)}")
    else:
        print("Não existe caminho entre os pontos especificados.")
```

### 3.3 Algoritmos de Busca em Ambientes Complexos

Ambientes complexos apresentam desafios adicionais em relação à busca clássica, como a necessidade de otimizar uma função objetivo sem se preocupar com o caminho, lidar com múltiplos agentes com objetivos conflitantes, agir sob incerteza ou com informações parciais. Russell e Norvig (2013) abordam diversas técnicas para esses cenários:

*   **Busca Local (Local Search):** Utilizada principalmente em problemas de otimização, onde o objetivo é encontrar o estado com o melhor valor de uma função objetivo, e o caminho até ele não importa. Esses algoritmos mantêm apenas um estado atual (ou um pequeno conjunto) e tentam melhorá-lo movendo-se para estados vizinhos.
    *   *Subida de Encosta (Hill Climbing):* Move-se continuamente em direção a um valor crescente da função objetivo. É simples e eficiente em memória, mas suscetível a máximos locais, platôs e cumeeiras.
    *   *Subida de Encosta com Reinício Aleatório (Random-Restart Hill Climbing):* Executa a subida de encosta múltiplas vezes a partir de estados iniciais aleatórios para aumentar a chance de encontrar o ótimo global.
    *   *Recozimento Simulado (Simulated Annealing):* Permite movimentos para estados piores com uma probabilidade que diminui ao longo do tempo (controlada por uma "temperatura"), ajudando a escapar de máximos locais.
    *   *Busca de Feixe Local (Local Beam Search):* Mantém `k` estados em paralelo. Em cada passo, gera todos os sucessores dos `k` estados e seleciona os `k` melhores sucessores para a próxima iteração. É menos suscetível a máximos locais que a subida de encosta simples.
    *   *Busca de Feixe Local Estocástica (Stochastic Beam Search):* Similar à busca de feixe local, mas escolhe os `k` sucessores com probabilidade proporcional à sua qualidade, introduzindo aleatoriedade.

#### 3.3.1 Implementação da Busca de Feixe Local Estocástica (Stochastic Beam Search)

A Busca de Feixe Local Estocástica é uma variação da busca de feixe local que introduz aleatoriedade na seleção dos sucessores. Em vez de sempre escolher os k melhores sucessores, ela seleciona k sucessores com probabilidade proporcional à sua qualidade, o que ajuda a escapar de máximos locais.

```python
import random
import numpy as np
import matplotlib.pyplot as plt

def busca_feixe_estocastica(funcao_objetivo, estado_inicial, gerar_vizinhos, k=3, max_iteracoes=1000):
    """
    Implementação da Busca de Feixe Local Estocástica para maximização.
    
    Args:
        funcao_objetivo: Função que avalia a qualidade de um estado
        estado_inicial: Estado a partir do qual iniciar a busca
        gerar_vizinhos: Função que gera estados vizinhos de um estado dado
        k: Número de estados a manter em cada iteração (tamanho do feixe)
        max_iteracoes: Número máximo de iterações permitidas
    
    Returns:
        Tupla (melhor_estado, melhor_valor, historico)
    """
    # Inicializa o feixe com k cópias do estado inicial
    feixe = [estado_inicial] * k
    valores = [funcao_objetivo(estado) for estado in feixe]
    
    # Para rastrear o melhor estado encontrado
    melhor_estado = estado_inicial
    melhor_valor = funcao_objetivo(estado_inicial)
    
    # Para visualização do progresso
    historico = [(estado_inicial, melhor_valor)]
    
    print(f"Iniciando Busca de Feixe Estocástica com k={k}")
    print(f"Estado inicial: {estado_inicial}, Valor: {melhor_valor}")
    
    for i in range(max_iteracoes):
        # Gera todos os sucessores possíveis
        todos_sucessores = []
        for estado in feixe:
            sucessores = gerar_vizinhos(estado)
            todos_sucessores.extend(sucessores)
        
        # Avalia todos os sucessores
        valores_sucessores = [funcao_objetivo(s) for s in todos_sucessores]
        
        # Normaliza os valores para usar como probabilidades
        valores_norm = np.array(valores_sucessores)
        valores_norm = valores_norm - np.min(valores_norm) + 1e-10  # Evita valores negativos
        probabilidades = valores_norm / np.sum(valores_norm)
        
        # Seleciona k sucessores estocasticamente
        indices_selecionados = np.random.choice(
            len(todos_sucessores),
            size=k,
            p=probabilidades,
            replace=False
        )
        
        # Atualiza o feixe
        feixe = [todos_sucessores[idx] for idx in indices_selecionados]
        valores = [valores_sucessores[idx] for idx in indices_selecionados]
        
        # Atualiza o melhor estado encontrado
        max_valor = max(valores)
        if max_valor > melhor_valor:
            melhor_valor = max_valor
            melhor_estado = feixe[valores.index(max_valor)]
            print(f"Iteração {i+1}: Novo melhor valor encontrado: {melhor_valor}")
        
        # Registra o progresso
        historico.append((melhor_estado, melhor_valor))
        
        # Verifica convergência
        if len(set(map(tuple, feixe))) == 1:
            print(f"Convergência atingida após {i+1} iterações!")
            break
    
    print(f"\nResultado final:")
    print(f"Melhor estado: {melhor_estado}")
    print(f"Melhor valor: {melhor_valor}")
    
    return melhor_estado, melhor_valor, historico

# Exemplo: Encontrar o máximo da função f(x,y) = -(x^2 + y^2) + 4
# O máximo global está em (0,0) com valor 4

def funcao_objetivo(ponto):
    """Função objetivo a ser maximizada: f(x,y) = -(x^2 + y^2) + 4"""
    x, y = ponto
    return -(x**2 + y**2) + 4

def gerar_vizinhos(ponto, passo=0.1):
    """Gera pontos vizinhos em uma grade 2D"""
    x, y = ponto
    vizinhos = [
        (x + passo, y),
        (x - passo, y),
        (x, y + passo),
        (x, y - passo),
        (x + passo, y + passo),
        (x - passo, y - passo),
        (x + passo, y - passo),
        (x - passo, y + passo)
    ]
    return vizinhos

# Executa o algoritmo
if __name__ == "__main__":
    # Ponto inicial aleatório entre -2 e 2
    estado_inicial = (random.uniform(-2, 2), random.uniform(-2, 2))
    
    # Executa a busca de feixe estocástica
    melhor_estado, melhor_valor, historico = busca_feixe_estocastica(
        funcao_objetivo, estado_inicial, gerar_vizinhos, k=3
    )
    
    # Visualiza o progresso
    estados = [h[0] for h in historico]
    valores = [h[1] for h in historico]
    
    # Cria uma malha para visualizar a função objetivo
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = -(X**2 + Y**2) + 4
    
    # Plota a superfície e o caminho percorrido
    plt.figure(figsize=(12, 6))
    
    # Superfície 3D
    ax1 = plt.subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    x_path = [e[0] for e in estados]
    y_path = [e[1] for e in estados]
    z_path = valores
    ax1.plot(x_path, y_path, z_path, 'r-o', linewidth=2, markersize=5)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('f(X,Y)')
    ax1.set_title('Trajetória da Busca de Feixe Estocástica em 3D')
    
    # Contorno 2D com caminho
    ax2 = plt.subplot(122)
    contour = ax2.contourf(X, Y, Z, 20, cmap='viridis')
    ax2.plot(x_path, y_path, 'r-o', linewidth=2, markersize=5)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('Trajetória da Busca de Feixe Estocástica (Vista Superior)')
    plt.colorbar(contour, ax=ax2)
    
    plt.tight_layout()
    plt.savefig('stochastic_beam_search_visualization.png')
    plt.close()
    
    print(f"Visualização salva como 'stochastic_beam_search_visualization.png'")
```

### 3.4 Algoritmos Genéticos e Evolucionários

Os Algoritmos Genéticos (AGs) pertencem a uma classe mais ampla de algoritmos evolucionários, que se inspiram na evolução biológica para resolver problemas de busca e otimização. Eles operam sobre uma população de soluções candidatas, aplicando operadores como seleção, recombinação (cruzamento) e mutação para gerar novas populações com aptidão progressivamente maior. Russell e Norvig (2013) discutem essas abordagens no contexto da busca local estocástica e otimização:

*   **Algoritmos Genéticos (Genetic Algorithms - GAs):** Os AGs mantêm uma população de estados candidatos (representados como strings ou cromossomos) e geram a próxima geração combinando pares de indivíduos (cruzamento) e introduzindo pequenas alterações aleatórias (mutação). A seleção dos pais geralmente favorece indivíduos com maior aptidão (fitness), que mede a qualidade da solução representada pelo indivíduo.
*   **Programação Genética (Genetic Programming - GP):** Uma variante dos AGs onde os indivíduos na população são programas de computador (geralmente representados como árvores de expressão) em vez de strings. O objetivo é evoluir um programa que resolva uma tarefa específica. Os operadores de cruzamento e mutação são adaptados para manipular essas estruturas de programa.
*   **Estratégias de Evolução (Evolution Strategies - ES):** Outra abordagem evolucionária, frequentemente usada para otimização de parâmetros em espaços contínuos. Diferentemente dos AGs clássicos que operam em representações binárias ou discretas e enfatizam o cruzamento, as ES geralmente trabalham com vetores de números reais e focam mais na mutação (frequentemente usando distribuições gaussianas) e na seleção determinística ou probabilística dos melhores indivíduos (pais e/ou filhos) para formar a próxima geração.

#### 3.4.1 Implementação de um Algoritmo Genético Simples

Os Algoritmos Genéticos são métodos de busca inspirados na seleção natural e na genética. Eles mantêm uma população de soluções candidatas que evoluem ao longo de gerações através de operadores como seleção, cruzamento e mutação.

```python
import random
import numpy as np
import matplotlib.pyplot as plt

def algoritmo_genetico(funcao_fitness, tamanho_cromossomo, tamanho_populacao=100, 
                      taxa_cruzamento=0.8, taxa_mutacao=0.1, num_geracoes=100):
    """
    Implementação de um Algoritmo Genético simples para maximização.
    
    Args:
        funcao_fitness: Função que avalia a qualidade de um cromossomo
        tamanho_cromossomo: Número de genes em cada cromossomo
        tamanho_populacao: Número de indivíduos na população
        taxa_cruzamento: Probabilidade de cruzamento entre pares de indivíduos
        taxa_mutacao: Probabilidade de mutação de cada gene
        num_geracoes: Número de gerações a evoluir
    
    Returns:
        Tupla (melhor_individuo, melhor_fitness, historico_fitness)
    """
    # Inicializa a população aleatoriamente (0s e 1s)
    populacao = [
        [random.randint(0, 1) for _ in range(tamanho_cromossomo)]
        for _ in range(tamanho_populacao)
    ]
    
    # Para rastrear o progresso
    melhor_global = None
    melhor_fitness_global = -float('inf')
    historico_fitness = []
    
    print(f"Iniciando Algoritmo Genético com população de {tamanho_populacao} indivíduos")
    print(f"Tamanho do cromossomo: {tamanho_cromossomo}")
    print(f"Taxa de cruzamento: {taxa_cruzamento}, Taxa de mutação: {taxa_mutacao}")
    
    for geracao in range(num_geracoes):
        # Avalia a aptidão (fitness) de cada indivíduo
        fitness_valores = [funcao_fitness(individuo) for individuo in populacao]
        
        # Encontra o melhor indivíduo desta geração
        melhor_idx = fitness_valores.index(max(fitness_valores))
        melhor_individuo = populacao[melhor_idx]
        melhor_fitness = fitness_valores[melhor_idx]
        
        # Atualiza o melhor global se necessário
        if melhor_fitness > melhor_fitness_global:
            melhor_global = melhor_individuo.copy()
            melhor_fitness_global = melhor_fitness
        
        # Registra estatísticas
        fitness_medio = sum(fitness_valores) / len(fitness_valores)
        historico_fitness.append((geracao, melhor_fitness, fitness_medio))
        
        print(f"Geração {geracao+1}: Melhor fitness = {melhor_fitness}, Média = {fitness_medio:.2f}")
        
        # Cria a próxima geração
        nova_populacao = []
        
        # Elitismo: mantém o melhor indivíduo
        nova_populacao.append(melhor_individuo)
        
        # Preenche o resto da população com novos indivíduos
        while len(nova_populacao) < tamanho_populacao:
            # Seleção por torneio
            pai1 = selecao_torneio(populacao, fitness_valores)
            pai2 = selecao_torneio(populacao, fitness_valores)
            
            # Cruzamento
            if random.random() < taxa_cruzamento:
                filho1, filho2 = cruzamento(pai1, pai2)
            else:
                filho1, filho2 = pai1.copy(), pai2.copy()
                
            # Mutação
            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)
            
            # Adiciona à nova população
            nova_populacao.append(filho1)
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(filho2)
        
        # Substitui a população antiga pela nova
        populacao = nova_populacao
    
    print(f"\nMelhor solução encontrada:")
    print(f"Cromossomo: {melhor_global}")
    print(f"Fitness: {melhor_fitness_global}")
    
    return melhor_global, melhor_fitness_global, historico_fitness

def selecao_torneio(populacao, fitness_valores, tamanho_torneio=3):
    """Seleciona um indivíduo usando seleção por torneio"""
    indices_torneio = random.sample(range(len(populacao)), tamanho_torneio)
    indice_vencedor = max(indices_torneio, key=lambda i: fitness_valores[i])
    return populacao[indice_vencedor].copy()

def cruzamento(pai1, pai2):
    """Realiza cruzamento de um ponto entre dois pais"""
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutacao(cromossomo, taxa_mutacao):
    """Aplica mutação bit-flip com probabilidade taxa_mutacao para cada gene"""
    for i in range(len(cromossomo)):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i]  # Inverte o bit (0->1, 1->0)

# Exemplo: Problema da mochila
# Temos n itens, cada um com um peso e um valor.
# Queremos maximizar o valor total sem exceder a capacidade da mochila.

def fitness_mochila(cromossomo):
    """
    Função de fitness para o problema da mochila.
    Cromossomo é uma lista binária onde 1 indica que o item é selecionado.
    """
    # Pesos e valores dos itens
    pesos = [2, 3, 5, 7, 1, 4, 1, 3, 8, 9]
    valores = [5, 7, 10, 15, 3, 9, 2, 6, 16, 18]
    
    # Capacidade da mochila
    capacidade = 20
    
    # Calcula peso e valor total dos itens selecionados
    peso_total = sum(pesos[i] for i in range(len(cromossomo)) if cromossomo[i] == 1)
    valor_total = sum(valores[i] for i in range(len(cromossomo)) if cromossomo[i] == 1)
    
    # Penaliza soluções que excedem a capacidade
    if peso_total > capacidade:
        return 0  # ou alguma penalidade proporcional ao excesso
    
    return valor_total

# Executa o algoritmo
if __name__ == "__main__":
    # Número de itens no problema da mochila
    num_itens = 10
    
    # Executa o algoritmo genético
    melhor_solucao, melhor_fitness, historico = algoritmo_genetico(
        fitness_mochila, num_itens, tamanho_populacao=50, num_geracoes=100
    )
    
    # Visualiza o progresso
    geracoes = [h[0] for h in historico]
    melhores = [h[1] for h in historico]
    medias = [h[2] for h in historico]
    
    plt.figure(figsize=(10, 6))
    plt.plot(geracoes, melhores, 'r-', label='Melhor Fitness')
    plt.plot(geracoes, medias, 'b--', label='Fitness Médio')
    plt.xlabel('Geração')
    plt.ylabel('Fitness')
    plt.title('Evolução do Fitness ao Longo das Gerações')
    plt.legend()
    plt.grid(True)
    plt.savefig('genetic_algorithm_progress.png')
    plt.close()
    
    print(f"Visualização salva como 'genetic_algorithm_progress.png'")
    
    # Mostra os itens selecionados
    pesos = [2, 3, 5, 7, 1, 4, 1, 3, 8, 9]
    valores = [5, 7, 10, 15, 3, 9, 2, 6, 16, 18]
    
    itens_selecionados = [i for i in range(len(melhor_solucao)) if melhor_solucao[i] == 1]
    peso_total = sum(pesos[i] for i in itens_selecionados)
    valor_total = sum(valores[i] for i in itens_selecionados)
    
    print(f"\nItens selecionados: {itens_selecionados}")
    print(f"Peso total: {peso_total}/20")
    print(f"Valor total: {valor_total}")
```

## Referências Bibliográficas

RUSSELL, S. J.; NORVIG, P. *Inteligência artificial*. 3. ed. Rio de Janeiro: Elsevier Campus, 2013.

CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. *Introduction to Algorithms*. 3. ed. Cambridge: MIT Press, 2009.

KORF, R. E. Depth-first iterative-deepening: An optimal admissible tree search. *Artificial Intelligence*, v. 27, n. 1, p. 97-109, 1985.

HART, P. E.; NILSSON, N. J.; RAPHAEL, B. A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics*, v. 4, n. 2, p. 100-107, 1968.

KIRKPATRICK, S.; GELATT, C. D.; VECCHI, M. P. Optimization by simulated annealing. *Science*, v. 220, n. 4598, p. 671-680, 1983.

HOLLAND, J. H. *Adaptation in Natural and Artificial Systems*. Ann Arbor: University of Michigan Press, 1975.

KOZA, J. R. *Genetic Programming: On the Programming of Computers by Means of Natural Selection*. Cambridge: MIT Press, 1992.

SILVER, D. et al. Mastering the game of Go with deep neural networks and tree search. *Nature*, v. 529, n. 7587, p. 484-489, 2016.

THRUN, S.; BURGARD, W.; FOX, D. *Probabilistic Robotics*. Cambridge: MIT Press, 2005.

LAVALLE, S. M. *Planning Algorithms*. Cambridge: Cambridge University Press, 2006.


| Versão | Data       | Modificação         | Nome                 | GitHub                                      |
|--------|------------|---------------------|----------------------|---------------------------------------------|
| `1.0`  | 27/05/2025 | Criação do documento | Ana Beatriz Norberto | [@ananorberto](https://github.com/ananorberto) |

